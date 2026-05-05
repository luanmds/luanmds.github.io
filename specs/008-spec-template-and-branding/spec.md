# Spec 008 — Template único de specs + ajustes de branding

**Status:** in-progress  
**Data:** 2026-05-04  
**Objetivo:** Padronizar o formato das specs com `spec.md` + `tasks.md`, criar uma spec modelo para próximas iniciativas, adicionar ícone do GitHub na navbar e ajustar o branding do blog com título técnico seguro e marca visual no header.

## Contexto

O repositório já possui specs com formatos diferentes. Além da padronização de documentação, o blog precisa de dois ajustes finais de apresentação antes de ir ao ar.

## Escopo

1. Aplicar padrão único de spec em `specs/001` até `specs/007`.
2. Criar `specs/000-template/` como referência oficial para novas specs.
3. Adicionar link do GitHub com ícone na navegação principal PT/EN.
4. Atualizar título global e por idioma para `LuanMDS` e renderizar marca visual `< LuanMDS />` no header.

## Fora de escopo

- Redesenho completo do header/layout.
- Alterações em conteúdo dos artigos.
- Mudanças de CI/CD.

## Decisões aprovadas

- Template oficial fica em `specs/000-template/`.
- Specs legadas serão padronizadas retroativamente.
- Link de GitHub será exibido como ícone no menu principal, sem texto.
- Título técnico do blog definido como `LuanMDS` para SEO/metadados.
- Marca visual no header definida como `< LuanMDS />` com cores por tema.

## Critérios de aceitação

1. Todas as specs ativas possuem `spec.md` e `tasks.md`.
2. `specs/000-template/` documenta a estrutura padrão para novas specs.
3. Header PT/EN exibe ícone do GitHub apontando para `https://github.com/luanmds`.
4. Título técnico do blog está consistente em configuração global e por idioma.
5. Header renderiza a marca visual `< LuanMDS />` em light/dark com contraste adequado.

## Riscos e mitigação

- **Risco:** inconsistência residual entre specs antigas.  
  **Mitigação:** revisar `001` a `007` e garantir referência explícita para `tasks.md`.
- **Risco:** item de menu com comportamento visual divergente.  
  **Mitigação:** usar padrão de params já suportado pelo Congo (`icon`, `showName`, `target`).

## Artefatos previstos

- `hugo.toml`
- `specs/000-template/spec.md`
- `specs/000-template/tasks.md`
- `specs/008-spec-template-and-branding/spec.md`
- `specs/008-spec-template-and-branding/tasks.md`
- `specs/001-hugo-setup/tasks.md`
- `specs/002-multilingual/tasks.md`
- `specs/003-content-structure/tasks.md`
- `specs/005-deployment/tasks.md`
- Atualizações em specs `001` a `007`
- `AGENTS.md`

## Validação

- Build local de produção com Hugo extended:
  - `docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify`
- Verificação manual de navegação PT/EN para ícone de GitHub.

## Referência de tarefas

- Ver `specs/008-spec-template-and-branding/tasks.md`.

## Refinamento 8.1 — Branding visível no header

**Problema:** Definir `title` com caracteres de marcação (`<.../>`) pode resultar em comportamento indesejado no render do texto da marca no cabeçalho.

**Solução aprovada:**
- Renderizar o branding no `layouts/_partials/logo.html` com spans dedicados.
- Exibir visualmente `< LuanMDS />` no header.
- Aplicar cores diferentes para `<` e `/>` usando classes da paleta do Congo em light/dark (`text-primary-600 dark:text-primary-400`).
