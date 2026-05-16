# stack.md

## Gerador de Site Estático

| Tecnologia | Versão | Papel |
|---|---|---|
| **Hugo extended** | 0.154.5 | SSG — compila Markdown + templates em HTML estático |

Hugo **extended** é obrigatório. O tema Congo usa funcionalidades exclusivas da versão extended (transpile de SCSS via libsass embutida, processamento de imagens).

## Tema

| Tecnologia | Papel |
|---|---|
| **Congo** | Tema ativo. Git submodule de `jpanther/congo`. Fornece layouts, componentes, dark mode, busca e RSS nativos. |
| PaperMod | Submodule legado (não usado). Mantido temporariamente para rollback de emergência. |

## Linguagens de conteúdo

| Linguagem | Uso |
|---|---|
| **Markdown** | Todo o conteúdo de posts e páginas |
| **HTML (Go templates)** | Overrides de layout em `layouts/` |
| **TOML** | Configuração principal (`hugo.toml`) |
| **YAML** | Front matter dos posts e traduções i18n (`i18n/*.yaml`) |
| **CSS** | Customizações visuais em `assets/css/` |

## Infraestrutura e runtime

| Tecnologia | Papel |
|---|---|
| **GitHub Pages** | Hospedagem estática gratuita |
| **GitHub Actions** | CI/CD — build + deploy automático no push para `main` |
| **Docker** (`hugomods/hugo:exts`) | Ambiente de desenvolvimento local (`docker compose up`) |

## Busca

- **Fuse.js** — busca client-side. Nativo do Congo. Indexa via `JSON` output no `home`. Não requer servidor.

## Comentários

- **Giscus** — embed de comentários via GitHub Discussions. Configurado no `hugo.toml`, mas **DISABLED FOR NOW** — `repoId` e `categoryId` estão vazios. Veja `.docs/integrations.md` para instruções de ativação.

## Dependências externas de runtime

| Serviço | URL | Papel |
|---|---|---|
| giscus.app | `https://giscus.app/client.js` | Script de comentários (carregado no browser) |

## Ferramentas de desenvolvimento

| Ferramenta | Uso |
|---|---|
| Docker Compose | `docker compose up` para servidor local na porta 1313 |
| Git submodules | Gestão do tema Congo |
| CodeRabbit | Code review automatizado via `.coderabbit.yaml` em PRs prontos para review |
| OpenCode | Agente AI de desenvolvimento (descobre skills locais em `.agents/skills/`) |
| Compozy | Workflow opcional baseado em artefatos em `.compozy/tasks/` |

## Skills locais

As skills locais do repositório vivem em `.agents/skills/` e hoje se dividem em três grupos:

- referência: `compozy`
- workflow Compozy: `cy-create-prd`, `cy-create-techspec`, `cy-create-tasks`, `cy-execute-task`, `cy-review-round`, `cy-fix-reviews`, `cy-final-verify`, `cy-workflow-memory`
- utilidades do projeto: `playwright-skill`, `content-review`, `github-branch-pr`
