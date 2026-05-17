# testing.md

## Estratégia atual

Não há suite de testes automatizados em CI. A estratégia atual combina validação de build com validação manual de browser quando o escopo pede isso.

## Build obrigatório

O build de produção é o smoke test obrigatório do repositório. Ele captura:

- Templates com sintaxe inválida
- Referências a layouts ou partials inexistentes
- Front matter malformado que causa erro de build
- Configurações incompatíveis no `hugo.toml`

Comando:

```bash
docker run --rm -v $(pwd):/src -w /src hugomods/hugo:exts hugo --minify
```

O build **não garante** que o site funciona visualmente ou que links estão corretos — apenas que compila.

## Validação de browser

Para mudanças com impacto em UX, templates, navegação, responsividade ou qualquer comportamento visível no site:

1. Subir servidor local: `docker compose up -d`
2. Invocar a skill Playwright (`.agents/skills/playwright-skill/`)
3. Rodar testes contra `http://localhost:1313`
4. Corrigir falhas antes de prosseguir

## Quando oferecer Playwright

Após implementar mudanças com impacto em browser, pergunte ao usuário:

> "Would you like to validate the implementation with automated browser tests using the Playwright skill?"

Se sim: invocar a skill e rodar contra o servidor local antes do commit ou PR.

## O que não existe (e é ausência consciente)

- Testes unitários em CI para lógica de aplicação, porque o projeto é majoritariamente templates e conteúdo
- Testes de integração em CI com Playwright
- Verificação automática de links quebrados
- Testes automatizados de acessibilidade
- Testes de performance (Lighthouse, etc.)
