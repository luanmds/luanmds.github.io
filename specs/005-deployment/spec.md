# Spec 005 — Deploy GitHub Pages

**Status:** ✅ done  
**Objetivo:** Build e deploy automático no GitHub Pages via GitHub Actions.

## Contexto

O repositório `luanmds/luanmds.github.io` usa GitHub Pages com deploy via **GitHub Actions** (não o modo classic com branch `gh-pages`). Isso dá controle total sobre o processo de build.

## Workflow: `.github/workflows/deploy.yml`

```
push → main
  └── job: build
        ├── checkout (com --recurse-submodules para PaperMod)
        ├── peaceiris/actions-hugo@v3 (extended: true)
        ├── hugo --minify
        └── upload artifact (./public)
  └── job: deploy
        └── actions/deploy-pages@v4
```

## Ativação no GitHub

Para ativar o deploy:
1. Vá em **Settings → Pages** do repositório
2. Em **Source**, selecione **GitHub Actions**
3. Faça push para `main` — o workflow dispara automaticamente

## Versão do Hugo no CI

O workflow usa `HUGO_VERSION: 0.154.5` (mesma versão do Docker local) para garantir paridade entre dev e produção.

## Artefatos produzidos

| Arquivo | Descrição |
|---------|-----------|
| `.github/workflows/deploy.yml` | Workflow de build e deploy |

## Tasks concluídas

- [x] `.github/workflows/deploy.yml` criado com Hugo extended + Pages deploy
- [x] `baseURL = "https://luanmds.github.io/"` configurado no `hugo.toml`
- [x] Build `hugo --minify` local validado sem erros (31 pt + 20 en páginas)
- [ ] Verificar site ao vivo após primeiro push (pendente: requer push para main)
