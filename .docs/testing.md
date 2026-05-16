# testing.md

## Estratégia atual

Não há suite de testes automatizados em CI. A estratégia atual combina validação de build com validação manual de browser quando o escopo pede isso.

### 1. Build como smoke test obrigatório

O build do Hugo (`hugo --minify`) é executado pelo GitHub Actions a cada push em `main`. Se o build falhar, o deploy não acontece. Isso captura:

- Templates com sintaxe inválida
- Referências a layouts ou partials inexistentes
- Front matter malformado que causa erro de build
- Configurações incompatíveis no `hugo.toml`

O build **não garante** que o site funciona visualmente ou que links estão corretos — apenas que compila.

Para fechar mudanças relevantes no repositório, execute também localmente:

```bash
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

### 2. Playwright manual para mudanças com impacto em browser

Testes de browser são executados manualmente quando a mudança afeta UX, templates, navegação, responsividade ou qualquer comportamento visível no site. O processo:

1. Subir servidor local: `docker compose up -d`
2. Invocar a skill Playwright (`.agents/skills/playwright-skill/`)
3. Rodar testes contra `http://localhost:1313`
4. Corrigir falhas antes de prosseguir

A skill local está disponível em `.agents/skills/playwright-skill/` e o servidor de dev deve estar ativo antes de usá-la. O OpenCode descobre esse diretório nativamente, sem ajustes adicionais no `opencode.json`.

---

## Quando oferecer Playwright

Após implementar mudanças com impacto em browser, pergunte ao usuário:

> "Would you like to validate the implementation with automated browser tests using the Playwright skill?"

Se sim: invocar a skill e rodar contra o servidor local antes do commit ou PR.

---

## O que não existe (e é ausência consciente)

- Testes unitários em CI para lógica de aplicação, porque o projeto é majoritariamente templates e conteúdo
- Testes de integração em CI com Playwright
- Verificação automática de links quebrados
- Testes automatizados de acessibilidade
- Testes de performance (Lighthouse, etc.)

---

## Como testar localmente

```bash
# Subir servidor de desenvolvimento
docker compose up

# Build de produção para validar antes de publicar
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

O build de produção deve ser executado pelo menos uma vez antes de criar PR em mudanças relevantes, pois o servidor de dev (`hugo server`) é mais permissivo que o build final.
