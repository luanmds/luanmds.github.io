# integrations.md

## GitHub Pages

**Tipo:** Hospedagem estática  
**URL de produção:** `https://luanmds.github.io/`  
**Integração:** O GitHub Actions faz deploy automaticamente após o build bem-sucedido. Não há configuração adicional além do workflow `.github/workflows/deploy.yml` e das permissões no repositório (Settings > Pages > Source: GitHub Actions).

**Dependência:** O repositório deve ter GitHub Pages habilitado com source "GitHub Actions".

---

## GitHub Actions

**Tipo:** CI/CD  
**Arquivo:** `.github/workflows/deploy.yml`  
**Trigger:** Push em `main` ou `workflow_dispatch` (manual)  

**Actions usadas:**

| Action | Versão | Função |
|---|---|---|
| `actions/checkout@v4` | v4 | Checkout com submodules recursivos |
| `peaceiris/actions-hugo@v3` | v3 | Instala Hugo extended |
| `actions/configure-pages@v5` | v5 | Configura o ambiente do GitHub Pages |
| `actions/upload-pages-artifact@v3` | v3 | Upload do artefato de build |
| `actions/deploy-pages@v4` | v4 | Deploy para GitHub Pages |

**Sem notificações de falha configuradas.** Falhas só são visíveis na aba Actions do repositório.

---

## Giscus

**Tipo:** Sistema de comentários via GitHub Discussions  
**Status: DISABLED FOR NOW — parcialmente implementado, mas não funcional**  
**Script:** `https://giscus.app/client.js` (carregado no browser)

> ⚠️ Os comentários não aparecem em nenhum post enquanto `repoId` e `categoryId` estiverem vazios. Esta é a fonte de verdade para reativar o Giscus no futuro.

**Configuração necessária (em `hugo.toml`):**

```toml
[params.giscus]
  repo = "luanmds/luanmds.github.io"
  repoId = ""         # ← preencher em giscus.app
  category = "Announcements"
  categoryId = ""     # ← preencher em giscus.app
```

**Para ativar:**
1. Habilitar GitHub Discussions no repositório
2. Acessar [giscus.app](https://giscus.app), configurar e copiar `repoId` e `categoryId`
3. Preencher os valores no `hugo.toml`
4. Commitar e fazer deploy

O partial `layouts/_partials/comments.html` só renderiza o script se `repoId` e `categoryId` estiverem preenchidos — enquanto estiverem vazios, nenhum script é carregado.

---

## Docker / hugomods

**Tipo:** Ambiente de desenvolvimento local  
**Imagem:** `hugomods/hugo:exts` (Hugo extended, sem versão fixada no compose)  
**Comando:** `docker compose up` → servidor em `http://localhost:1313` com live reload

**Observação:** A imagem do Docker Compose não está fixada na mesma versão do Hugo usada no CI (0.154.5). Uma atualização da imagem `exts` pode introduzir divergências entre o comportamento local e o de produção.

---

## CodeRabbit

**Tipo:** Code review automatizado via GitHub  
**Configuração:** `.coderabbit.yaml`  
**Integração:** Comenta em PRs automaticamente com sugestões de revisão. Não bloqueia deploy.

---

## Dependências de runtime no browser

| Recurso | URL | Carregado quando |
|---|---|---|
| Giscus script | `https://giscus.app/client.js` | Em posts com comentários habilitados (quando configurado) |
| Fuse.js | Bundled pelo Congo | Na página de busca |

Não há outras chamadas de API externas. O site funciona 100% sem JavaScript para leitura de conteúdo (JS habilita busca, comentários e troca de tema).
