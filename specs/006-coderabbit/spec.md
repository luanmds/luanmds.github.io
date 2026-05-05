# Spec 006 — CodeRabbit Configuration

**Status:** done  
**Data:** 2026-05-04 (padronização)  
**Objetivo:** Configurar revisão automatizada de Pull Requests com CodeRabbit no repositório `luanmds/luanmds.github.io`.

## Contexto

CodeRabbit complementa revisão humana em PRs com foco em qualidade, manutenção e consistência de configuração.

## Escopo

1. Adicionar configuração versionada do CodeRabbit.
2. Definir comportamento padrão para revisão automática.
3. Reduzir ruído ignorando paths gerados.

## Fora de escopo

- Substituir revisão humana.
- Alterar pipeline de deploy.
- Configurar branch protection.

## Decisões aprovadas

- Opção selecionada: GitHub App + `.coderabbit.yaml`.
- Idioma dos reviews definido para `en-US`.
- Paths gerados ignorados (`public/**`, `resources/**`).

## Critérios de aceitação

1. `.coderabbit.yaml` válido no repositório.
2. PRs recebem análise automática.
3. Diretórios gerados não produzem comentários automáticos.
4. Sem regressão no workflow de deploy.

## Riscos e mitigação

- **Risco:** excesso de comentários em PRs grandes.  
  **Mitigação:** ajustar escopo por path no `.coderabbit.yaml`.
- **Risco:** App não instalado corretamente.  
  **Mitigação:** validar em Settings → Integrations.

## Artefatos previstos

- `specs/006-coderabbit/spec.md`
- `specs/006-coderabbit/tasks.md`
- `.coderabbit.yaml`

## Validação

- Abrir PR de teste e confirmar comentários automáticos esperados.

## Referência de tarefas

- Ver `specs/006-coderabbit/tasks.md`.
