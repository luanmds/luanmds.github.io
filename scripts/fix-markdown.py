#!/usr/bin/env python3
"""
fix-markdown.py - Post-process Pandoc-converted Markdown files.

Fixes applied:
  1. Loose lists → tight lists (removes blank lines between list items)
  2. HTML <img> tags (single/multi-line) → Markdown image syntax
  3. Strips <u> / </u> underline tags (Google Docs underlined links artifact)
  4. Removes Pandoc backslash escapes inside fenced code blocks
  5. Removes blank lines inside code fences (Pandoc paragraph-per-line artifact)
  6. Removes trailing backslash hard line breaks from prose (Google Docs wrap artifact)
  7. Unwraps hard-wrapped prose lines (Pandoc ~72-char wrapping artifact)

Usage:
  python3 fix-markdown.py content/posts/slug/index.md [...]
"""

import re
import sys
from pathlib import Path

# Markdown special characters that Pandoc escapes in DOCX→GFM conversion.
# Inside code fences these escapes are incorrect — raw chars are needed.
_PANDOC_ESCAPE_RE = re.compile(r'\\([\[\]<>_()*{}|!$#@~])')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_list_item(line: str) -> bool:
    """Unordered or ordered list item at any indentation level."""
    return bool(re.match(r'^\s*[-*+]\s', line)) or bool(re.match(r'^\s*\d+\.\s', line))


def is_list_related(line: str) -> bool:
    """List item OR indented continuation line (≥2 spaces of indent + content)."""
    return is_list_item(line) or bool(re.match(r'^\s{2,}\S', line))


# ---------------------------------------------------------------------------
# Fix 1: Tighten loose lists
# ---------------------------------------------------------------------------

def tighten_lists(lines: list[str]) -> list[str]:
    """
    Remove blank lines that sit between consecutive list-related lines.

    A blank line is removed when:
      - the next non-blank line is a list item, AND
      - the previous non-blank line is list-related (item or continuation).

    Blank lines that separate paragraphs from lists, or lists from paragraphs,
    are preserved.
    """
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip() == '':
            # Scan back for previous non-blank line
            prev_idx = i - 1
            while prev_idx >= 0 and lines[prev_idx].strip() == '':
                prev_idx -= 1

            # Scan forward for next non-blank line
            next_idx = i + 1
            while next_idx < len(lines) and lines[next_idx].strip() == '':
                next_idx += 1

            prev_line = lines[prev_idx] if prev_idx >= 0 else ''
            next_line = lines[next_idx] if next_idx < len(lines) else ''

            # Drop blank line only when it sits between list content
            if is_list_item(next_line) and is_list_related(prev_line):
                i += 1
                continue  # skip this blank line

        result.append(line)
        i += 1

    return result


# ---------------------------------------------------------------------------
# Fix 2: HTML <img> → Markdown image
# ---------------------------------------------------------------------------

# Matches single- and multi-line <img> tags that contain a src attribute.
_IMG_RE = re.compile(
    r'<img\b[^>]*?\bsrc=["\']([^"\']+)["\'][^>]*/?>',
    re.DOTALL | re.IGNORECASE,
)


def fix_img_tags(content: str) -> str:
    """
    Replace <img src="image3.png" style="..."> with ![](image3.png).
    Preserves the leading whitespace of the opening <img tag so that images
    inside list items stay properly indented.
    """
    # We need to track leading whitespace before <img to keep indentation.
    pattern = re.compile(
        r'([ \t]*)<img\b[^>]*?\bsrc=["\']([^"\']+)["\'][^>]*/?>',
        re.DOTALL | re.IGNORECASE,
    )

    def replace(m: re.Match) -> str:
        indent = m.group(1)
        src = m.group(2)
        filename = src.split('/')[-1]  # keep only the filename
        return f'{indent}![]({filename})'

    return pattern.sub(replace, content)


# ---------------------------------------------------------------------------
# Fix 3: Strip <u> / </u> tags
# ---------------------------------------------------------------------------

_UNDERLINE_RE = re.compile(r'</?u>', re.IGNORECASE)


def strip_underline_tags(content: str) -> str:
    return _UNDERLINE_RE.sub('', content)


# ---------------------------------------------------------------------------
# Fix 4: Remove Pandoc escape backslashes inside code fences
# ---------------------------------------------------------------------------

def unescape_code_fences(content: str) -> str:
    """
    Within fenced code blocks (```...```), remove backslash escapes that
    Pandoc adds when converting DOCX → GFM.

    Examples fixed:
      \\[Fact\\]          →  [Fact]
      \\_fixture          →  _fixture
      \\<Customer\\>      →  <Customer>
      =\\>                →  =>
      Mock\\<IFoo\\>      →  Mock<IFoo>

    Trailing backslashes at end of a line (Markdown hard line break) are
    intentionally left alone — they are outside code fences in normal prose.
    """
    parts: list[str] = []
    # Split on fence delimiters, keeping them as tokens.
    # Pattern matches opening fences: optional spaces + 3+ backticks + optional lang + newline
    segments = re.split(r'(^ *`{3,}[^\n]*\n)', content, flags=re.MULTILINE)

    in_fence = False
    fence_marker = ''

    for segment in segments:
        if not in_fence:
            # Check if this segment is an opening fence
            fence_match = re.match(r'^( *`{3,})[^\n]*\n$', segment)
            if fence_match:
                in_fence = True
                fence_marker = fence_match.group(1).strip()  # e.g. "```"
                parts.append(segment)
            else:
                parts.append(segment)
        else:
            # We're inside a fence — look for the closing fence
            close_re = re.compile(
                r'^( *' + re.escape(fence_marker) + r'`*\s*$)',
                re.MULTILINE,
            )
            close_match = close_re.search(segment)
            if close_match:
                # Split into: code body | closing fence | rest
                code_body = segment[:close_match.start()]
                closing = segment[close_match.start():close_match.end()]
                rest = segment[close_match.end():]

                clean_body = _PANDOC_ESCAPE_RE.sub(r'\1', code_body)
                parts.append(clean_body)
                parts.append(closing)
                parts.append(rest)
                in_fence = False
                fence_marker = ''
            else:
                # No closing fence yet (shouldn't happen in valid MD)
                parts.append(_PANDOC_ESCAPE_RE.sub(r'\1', segment))

    return ''.join(parts)


# ---------------------------------------------------------------------------
# Fix 5: Remove blank lines inside fenced code blocks
# ---------------------------------------------------------------------------

def tighten_code_fences(content: str) -> str:
    """
    Remove blank lines that appear between every code line inside a fenced
    code block — a known Pandoc artifact when converting DOCX paragraphs.

    Blank lines that are part of the surrounding prose are preserved.
    """
    result: list[str] = []
    in_fence = False

    for line in content.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            result.append(line)
            continue

        if in_fence and line.strip() == '':
            continue  # drop blank lines inside code fences

        result.append(line)

    return '\n'.join(result)


# ---------------------------------------------------------------------------
# Fix 6: Remove trailing backslash hard line breaks from prose
# ---------------------------------------------------------------------------

def remove_trailing_hard_breaks(content: str) -> str:
    """
    Remove trailing `\\` that Pandoc inserts as Markdown hard line breaks
    for line wraps that existed inside Google Docs paragraphs.

    Only removes from prose — lines inside code fences are left alone.
    Does NOT remove `\\\\` (escaped backslash).
    """
    result: list[str] = []
    in_fence = False

    for line in content.split('\n'):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            result.append(line)
            continue

        if not in_fence and line.endswith('\\') and not line.endswith('\\\\'):
            line = line[:-1]  # strip the single trailing backslash

        result.append(line)

    return '\n'.join(result)


# ---------------------------------------------------------------------------
# Fix 7: Unwrap hard-wrapped prose lines
# ---------------------------------------------------------------------------

def _is_special_for_unwrap(line: str) -> bool:
    """
    Return True for lines that must NOT be joined to an adjacent prose line:
    blank, headings, list items, images, block quotes, HTML blocks,
    horizontal rules, and code fences.

    NOTE: list items are flagged here so that the main loop can handle them
    in their own branch (which joins continuation lines).
    """
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith('```'):
        return True
    if re.match(r'^#{1,6}\s', stripped):
        return True
    # Unordered and ordered list items (not indented continuations)
    if re.match(r'^[-*+]\s', stripped) or re.match(r'^\d+\.\s', stripped):
        return True
    if stripped.startswith('!['):
        return True
    if stripped.startswith('>'):
        return True
    if re.match(r'^<[a-zA-Z/!]', stripped):
        return True
    # Horizontal rules (--- / *** / ___)
    if re.match(r'^[-*_]{3,}\s*$', stripped):
        return True
    return False


def _is_list_item_line(line: str) -> bool:
    stripped = line.strip()
    return bool(re.match(r'^[-*+]\s', stripped)) or bool(re.match(r'^\d+\.\s', stripped))


def _is_list_continuation_line(line: str) -> bool:
    """Line indented with ≥2 spaces followed by a non-space (list item continuation)."""
    return bool(re.match(r'^\s{2,}\S', line))


def unwrap_prose(content: str) -> str:
    """
    Join hard-wrapped prose lines within the same paragraph into a single line.

    Pandoc wraps output at ~72 chars. This reverses that so each paragraph
    is one long line, which is easier to read as source and diff cleanly.

    Rules:
    - Front matter (between --- delimiters) is left untouched.
    - Content inside fenced code blocks is left untouched.
    - Blank lines (paragraph separators) are preserved.
    - Special lines (headings, images, block quotes, HTML, HRs) are kept as-is.
    - List items have their indented continuation lines joined onto them.
    - Regular prose lines are joined forward until a blank or special line is hit.
    """
    lines = content.split('\n')
    result: list[str] = []
    in_fence = False
    in_front_matter = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Front matter ────────────────────────────────────────────────────
        if i == 0 and stripped == '---':
            in_front_matter = True
            result.append(line)
            i += 1
            continue

        if in_front_matter:
            result.append(line)
            if stripped == '---':
                in_front_matter = False
            i += 1
            continue

        # ── Code fence ──────────────────────────────────────────────────────
        if stripped.startswith('```'):
            in_fence = not in_fence
            result.append(line)
            i += 1
            continue

        if in_fence:
            result.append(line)
            i += 1
            continue

        # ── Blank line ──────────────────────────────────────────────────────
        if not stripped:
            result.append(line)
            i += 1
            continue

        # ── List item: join with indented continuation lines ─────────────────
        if _is_list_item_line(line):
            accumulated = line.rstrip()
            while i + 1 < len(lines) and _is_list_continuation_line(lines[i + 1]):
                i += 1
                accumulated += ' ' + lines[i].strip()
            result.append(accumulated)
            i += 1
            continue

        # ── Other special lines (headings, images, etc.) ─────────────────────
        if _is_special_for_unwrap(line):
            result.append(line)
            i += 1
            continue

        # ── Orphan continuation line (shouldn't occur, but be safe) ──────────
        if _is_list_continuation_line(line):
            result.append(line)
            i += 1
            continue

        # ── Regular prose: join wrapped lines forward ─────────────────────────
        accumulated = line.rstrip()
        while i + 1 < len(lines):
            next_line = lines[i + 1]
            if (not next_line.strip()
                    or _is_special_for_unwrap(next_line)
                    or _is_list_continuation_line(next_line)):
                break
            i += 1
            accumulated += ' ' + next_line.strip()

        result.append(accumulated)
        i += 1

    return '\n'.join(result)


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process_file(path: Path) -> tuple[bool, list[str]]:
    """
    Apply all fixes to a single Markdown file.
    Returns (was_changed, list_of_applied_fix_names).
    """
    original = path.read_text(encoding='utf-8')
    content = original

    applied: list[str] = []

    # Fix 2 & 3 work on the full string (handle multi-line tags)
    new_content = fix_img_tags(content)
    if new_content != content:
        applied.append('img→markdown')
        content = new_content

    new_content = strip_underline_tags(content)
    if new_content != content:
        applied.append('strip-<u>')
        content = new_content

    new_content = unescape_code_fences(content)
    if new_content != content:
        applied.append('unescape-code-fences')
        content = new_content

    new_content = tighten_code_fences(content)
    if new_content != content:
        applied.append('tighten-code-fences')
        content = new_content

    new_content = remove_trailing_hard_breaks(content)
    if new_content != content:
        applied.append('remove-hard-breaks')
        content = new_content

    new_content = unwrap_prose(content)
    if new_content != content:
        applied.append('unwrap-prose')
        content = new_content

    # Fix 1 works line-by-line
    lines = content.split('\n')
    new_lines = tighten_lists(lines)
    if new_lines != lines:
        applied.append('tighten-lists')
        content = '\n'.join(new_lines)

    changed = content != original
    if changed:
        path.write_text(content, encoding='utf-8')

    return changed, applied


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: fix-markdown.py <file> [file2 ...]')
        sys.exit(1)

    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f'  SKIP  {path}')
            continue

        changed, fixes = process_file(path)
        if changed:
            print(f'  fixed [{", ".join(fixes)}]  →  {path}')
        else:
            print(f'  ok (no changes)  →  {path}')
