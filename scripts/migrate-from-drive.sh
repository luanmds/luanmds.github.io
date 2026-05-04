#!/usr/bin/env bash
# migrate-from-drive.sh
# Migrates Google Docs articles to Hugo page bundles.
# Requirements: ~/bin/pandoc, gio, curl, gdbus

set -euo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BLOG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="/tmp/hugo-migrate"
TODAY=$(date +%Y-%m-%d)
PANDOC="${HOME}/bin/pandoc"
DRIVE_EXPORT_URL="https://www.googleapis.com/drive/v3/files"
EXPORT_MIME="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
GOA_ACCOUNT_PATH="/org/gnome/OnlineAccounts/Accounts/account_1751138632_0"

# ---------------------------------------------------------------------------
# Article definitions
# FORMAT: "DRIVE_FILE_ID|TITLE|LANG|SLUG|TAGS(comma-sep)|TRANSLATION_KEY"
# TRANSLATION_KEY is empty for articles without an EN/PT pair.
# ---------------------------------------------------------------------------
ARTICLES=(
  "1XlKzhy_s8_YWszQldJRoKDFmLMyCbrD7IUEC2-iV5x0|Testes de Integração: Visão Geral e Boas Práticas|pt|testes-integracao-visao-geral|testes|integration-tests"
  "1dxfePBZjVa_jNRBnsrQfRNxyzcrwSeVuC-aEhXEFMXQ|Integration Tests: An Overview and Best Practices|en|integration-tests-overview|testing|integration-tests"
  "1U3QU1mTEQquPxcWxgLpdHlKcHguz9zyF8Qmyir9BOE8|Boas práticas em Unit Tests com .Net: A Teoria|pt|unit-tests-dotnet-teoria|testes,dotnet|"
  "1QCLZB_tMKRqAnDLwcOaoZt7YrFRS0f8wju0zero418M|Boas práticas em Unit Tests com .Net: A Prática|pt|unit-tests-dotnet-pratica|testes,dotnet|"
  "1t6st5QMyorUiHRa8TjyZ0qxfhjkRlxNnkeRI11VsweY|Saga Pattern - Um resumo com Caso de Uso|pt|saga-pattern-resumo|system-design|saga-pattern"
  "100BTKdyt96NLDD677DbtYiFF-Bnsn9dm6ouEFwTrNRE|Saga Pattern - An overview with use case|en|saga-pattern-overview|system-design|saga-pattern"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
log()     { echo "[migrate] $*"; }
success() { echo "[migrate] ✓ $*"; }
warn()    { echo "[migrate] ⚠ $*"; }
fail()    { echo "[migrate] ✗ $*" >&2; }

get_token() {
  gdbus call --session \
    --dest org.gnome.OnlineAccounts \
    --object-path "$GOA_ACCOUNT_PATH" \
    --method org.gnome.OnlineAccounts.OAuth2Based.GetAccessToken 2>/dev/null \
    | grep -oP "'\K[^']+(?=')" | head -1
}

# Build YAML tags block from comma-separated string
build_tags_yaml() {
  local tags_str="$1"
  local yaml=""
  IFS=',' read -ra tag_arr <<< "$tags_str"
  for t in "${tag_arr[@]}"; do
    t="${t// /}"  # trim spaces
    yaml+="  - ${t}"$'\n'
  done
  echo "$yaml"
}

# Rewrite absolute image paths in MD to relative filenames
rewrite_image_paths() {
  local md_file="$1"
  local img_tmp_dir="$2"
  # Replace absolute/relative paths to extracted images with just the filename
  # Handles both Markdown and HTML img tags produced by pandoc
  sed -i \
    -e "s|${img_tmp_dir}/media/||g" \
    -e 's|/tmp/hugo-migrate/[^/]*/media/||g' \
    "$md_file"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
mkdir -p "$TMP_DIR"

log "Fetching GOA access token..."
TOKEN=$(get_token)
if [[ -z "$TOKEN" ]]; then
  fail "Could not retrieve GOA access token. Is GNOME Online Accounts set up?"
  exit 1
fi
success "Token obtained."

FAILED_ARTICLES=()

for article in "${ARTICLES[@]}"; do
  IFS='|' read -r drive_id title lang slug tags translation_key <<< "$article"

  log "─────────────────────────────────────────"
  log "Article : $title"
  log "Lang    : $lang | Slug: $slug"

  docx_file="${TMP_DIR}/${slug}.docx"
  md_file="${TMP_DIR}/${slug}.md"
  img_dir="${TMP_DIR}/${slug}-images"

  # ── 1. Export from Drive ────────────────────────────────────────────────
  log "  Exporting from Google Drive..."
  http_code=$(curl -s -L \
    -H "Authorization: Bearer $TOKEN" \
    "${DRIVE_EXPORT_URL}/${drive_id}/export?mimeType=${EXPORT_MIME}" \
    -o "$docx_file" \
    -w "%{http_code}")

  if [[ "$http_code" != "200" ]]; then
    warn "Drive export failed (HTTP $http_code) for: $title"
    warn "Fallback (Approach C): export this doc manually as DOCX and place it at:"
    warn "  $docx_file"
    warn "Then re-run this script."
    FAILED_ARTICLES+=("$title")
    continue
  fi
  success "  Exported ($(du -sh "$docx_file" | cut -f1))"

  # ── 2. Convert to Markdown ──────────────────────────────────────────────
  log "  Converting to Markdown with Pandoc..."
  mkdir -p "$img_dir"
  "$PANDOC" "$docx_file" \
    -t gfm \
    --extract-media="$img_dir" \
    -o "$md_file" 2>/dev/null
  success "  Converted ($(wc -l < "$md_file") lines)"

  img_count=$(find "$img_dir" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.webp" \) 2>/dev/null | wc -l)
  log "  Images found: $img_count"

  # Fix image paths to be relative (just filename)
  rewrite_image_paths "$md_file" "$img_dir"

  # ── 3. Create Hugo page bundle ──────────────────────────────────────────
  if [[ "$lang" == "en" ]]; then
    bundle_dir="${BLOG_DIR}/content/en/posts/${slug}"
  else
    bundle_dir="${BLOG_DIR}/content/posts/${slug}"
  fi
  mkdir -p "$bundle_dir"

  # ── 4. Write index.md with front matter ────────────────────────────────
  tags_yaml=$(build_tags_yaml "$tags")

  {
    echo "---"
    echo "title: \"${title}\""
    echo "date: ${TODAY}"
    echo "draft: true"
    echo "tags:"
    printf '%s' "$tags_yaml"
    echo ""
    if [[ -n "$translation_key" ]]; then
      echo "translationKey: \"${translation_key}\""
    fi
    echo "---"
    echo ""
    # Strip the H1 title from the body (it's already in front matter)
    sed '1{/^# /d}' "$md_file"
  } > "${bundle_dir}/index.md"

  # ── 5. Copy images into the bundle ─────────────────────────────────────
  if [[ "$img_count" -gt 0 ]]; then
    find "$img_dir" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.webp" \) \
      -exec cp {} "$bundle_dir/" \;
    success "  Copied $img_count image(s) to bundle"
  fi

  success "  Created: ${bundle_dir}/index.md"
done

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "════════════════════════════════════════"
echo " Migration complete"
echo "════════════════════════════════════════"
echo ""

if [[ ${#FAILED_ARTICLES[@]} -gt 0 ]]; then
  warn "The following articles FAILED and need manual export (Approach C):"
  for a in "${FAILED_ARTICLES[@]}"; do
    warn "  • $a"
  done
  echo ""
fi

echo "Next steps:"
echo "  1. Review Markdown — fix bold/italic artifacts and code blocks"
echo "  2. Set cover image: add 'cover:\\n  image: <filename>' in front matter"
echo "  3. Update publication dates (currently set to ${TODAY})"
echo "  4. Set 'draft: false' when ready to publish"
echo ""
echo "PT articles: ${BLOG_DIR}/content/posts/"
echo "EN articles: ${BLOG_DIR}/content/en/posts/"
