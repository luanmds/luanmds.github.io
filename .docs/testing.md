# testing.md

## Estratégia atual

Não há suite de testes automatizados em CI. A estratégia é composta de duas camadas:

### 1. Build como smoke test

O build do Hugo (`hugo --minify`) é executado pelo GitHub Actions a cada push em `main`. Se o build falhar, o deploy não acontece. Isso captura:

- Templates com sintaxe inválida
- Referências a layouts ou partials inexistentes
- Front matter malformado que causa erro de build
- Configurações incompatíveis no `hugo.toml`

O build **não garante** que o site funciona visualmente ou que links estão corretos — apenas que compila.

### 2. Playwright manual (via skill)

Testes de browser são executados manualmente quando invocados pela skill `playwright-skill`, antes de commitar ou criar PR. O processo:

1. Subir servidor local: `docker compose up -d`
2. Invocar a skill Playwright (`.opencode/skills/playwright/`)
3. Rodar testes contra `http://localhost:1313`
4. Corrigir falhas antes de prosseguir

A skill está disponível em `.opencode/skills/playwright/` e o servidor de dev deve estar ativo antes de usá-la.

---

## Quando rodar os testes Playwright

O fluxo SDD prevê perguntar ao usuário após cada implementação:

> "Gostaria de validar a implementação com testes automatizados de browser usando a skill Playwright?"

Se sim: invocar a skill e rodar contra o servidor local antes do commit.

---

## O que não existe (e é ausência consciente)

- Testes unitários — não há lógica de código, apenas templates e conteúdo
- Testes de integração em CI — nenhum workflow roda Playwright automaticamente
- Verificação de links quebrados — não há step de link-check no CI
- Testes de acessibilidade automatizados
- Testes de performance (Lighthouse, etc.)

---

## Como testar localmente

```bash
# Subir servidor de desenvolvimento
docker compose up

# Build de produção para validar antes de publicar
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

O build de produção deve ser executado pelo menos uma vez antes de criar PR, pois o servidor de dev (`hugo server`) é mais permissivo que o build final.
