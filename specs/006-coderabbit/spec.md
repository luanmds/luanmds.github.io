# Spec 006 — CodeRabbit Configuration

**Status:** ✅ done  
**Objetivo:** Configurar revisão automatizada de Pull Requests com CodeRabbit no repositório `luanmds/luanmds.github.io`.

## Contexto

CodeRabbit atua como revisor automático em PRs, gerando comentários de qualidade, segurança e manutenção. Para este projeto (Hugo + GitHub Pages), ele deve focar em mudanças de conteúdo, workflows e configuração sem bloquear deploy.

## Escopo

1. Adicionar arquivo de configuração `.coderabbit.yaml` na raiz do repositório.
2. Definir comportamento padrão para revisões em PRs.
3. Limitar escopo de revisão para evitar ruído em diretórios gerados automaticamente.
4. Documentar pré-requisito de instalação do GitHub App no repositório.

## Fora de escopo

- Substituir revisão humana por revisão automática.
- Alterar pipeline de deploy do GitHub Pages.
- Configurar regras de branch protection no GitHub.

## Decisão validada

Adoção confirmada:

### Opção A — GitHub App + `.coderabbit.yaml` (selecionada)

- Instalar o CodeRabbit GitHub App no repositório.
- Versionar regras no `.coderabbit.yaml`.
- Permite ajustes finos por diretório e por tipo de arquivo.

### Opção B — Apenas GitHub App (sem arquivo de config) (não selecionada)

- Instalar o App e usar comportamento padrão.
- Menor manutenção inicial, menos controle de ruído/escopo.

## Configuração aplicada

- Ativar revisão automática em PRs.
- Definir idioma dos reviews como `en-US`.
- Ignorar revisão em paths gerados/derivados:
  - `public/**`
  - `resources/**`
- Priorizar revisão em:
  - `.github/workflows/**`
  - `content/**`
  - `hugo.toml`
- Instruções por path escritas em inglês no `.coderabbit.yaml`.

## Critérios de aceitação

1. Repositório contém `.coderabbit.yaml` válido (quando escolhida a Opção A).
2. PR novo recebe análise do CodeRabbit automaticamente.
3. Arquivos em `public/**` e `resources/**` não geram comentários automáticos.
4. Nenhuma regressão no workflow existente `.github/workflows/deploy.yml`.

## Riscos e mitigação

- **Risco:** excesso de comentários em PRs grandes.  
  **Mitigação:** ajustar escopo e paths ignorados no `.coderabbit.yaml`.
- **Risco:** App não instalado corretamente.  
  **Mitigação:** validar instalação em Settings → Integrations antes do primeiro PR de teste.

## Artefatos previstos

- `specs/006-coderabbit/spec.md`
- `specs/006-coderabbit/tasks.md`
- `.coderabbit.yaml` (apenas se Opção A)
- Atualização opcional em `AGENTS.md` (somente se houver mudança arquitetural relevante)
