# concerns.md

## Riscos conhecidos

### 1. Atualizações do tema Congo (alto impacto)

**Risco:** Congo é um submodule externo (`jpanther/congo`). Updates do upstream podem introduzir mudanças breaking nos templates, classes CSS ou parâmetros de configuração. O projeto tem overrides em `layouts/` e `assets/` que podem parar de funcionar silenciosamente após um update.

**Manifestação:** Após `git submodule update --remote themes/congo`, o site pode ter visual quebrado ou features desaparecendo sem erros de build.

**Mitigação atual:** Nenhuma. O submodule não está fixado em uma tag/commit específica de forma deliberada.

**Ação recomendada:** Ao atualizar o Congo, sempre testar localmente com `docker compose up` e rodar Playwright antes de fazer push.

---

### 2. CI/CD sem alertas de falha

**Risco:** Se o GitHub Actions falhar (build quebrado, deploy falhou), não há notificação ativa. A falha só é visível na aba "Actions" do repositório.

**Manifestação:** Um post pode ser commitado em `main`, o CI falhar silenciosamente, e o autor só perceber que o site não foi atualizado se acessar manualmente a aba Actions ou verificar o site.

**Mitigação atual:** Nenhuma.

**Ação recomendada:** Configurar notificações de falha no GitHub (Settings > Notifications) ou adicionar step de notificação no workflow.

---

### 3. Giscus não configurado

**Risco:** O sistema de comentários está parcialmente implementado (`comments.html`, parâmetros no `hugo.toml`), mas `repoId` e `categoryId` estão vazios. Os comentários não aparecem em nenhum post.

**Manifestação:** Visualmente invisível — o partial simplesmente não renderiza nada. Usuários não têm como comentar.

**Mitigação atual:** O partial tem guarda condicional — não carrega scripts externos com valores vazios. Nenhum erro é gerado.

**Ação para resolver:** Habilitar GitHub Discussions no repo, configurar em [giscus.app](https://giscus.app) e preencher `repoId` e `categoryId` no `hugo.toml`.

---

### 4. Versão do Hugo divergente entre local e CI

**Risco:** O CI usa `hugo-version: 0.154.5` fixado no workflow. O `docker-compose.yml` usa a imagem `hugomods/hugo:exts` sem versão fixada. Se a imagem local for atualizada para uma versão mais nova do Hugo, pode haver comportamentos diferentes entre local e CI.

**Manifestação:** Algo funciona no `docker compose up` mas falha no build do CI (ou vice-versa).

**Mitigação atual:** Baixo risco imediato, mas é um débito latente.

---

## Débitos técnicos

### 5. Ausência de sistema de design

O CSS customizado em `assets/css/` é mínimo e não existe documentação de design tokens, paleta de cores ou tipografia definida. Customizações visuais futuras serão feitas de forma ad hoc, sem referência consistente.

**Impacto:** Inconsistência visual ao adicionar componentes ou customizar o tema ao longo do tempo.

---

### 6. PaperMod legado em themes/

O submodule `themes/PaperMod/` está presente mas não é usado (tema ativo é Congo). Foi mantido como fallback de emergência após a migração.

**Impacto:** Aumenta o tamanho do checkout (CI e local), adiciona ruído no `.gitmodules`.

**Ação recomendada:** Remover quando não houver mais necessidade de rollback.

---

### 7. Primeiro post desatualizado

O post `bem-vindo-ao-blog/index.md` menciona PaperMod como tema ("tema minimalista PaperMod"), mas o tema atual é Congo. O conteúdo está desatualizado em relação à stack atual.

---

### 8. Sem verificação de links quebrados

Não há passo de link check no CI. Links externos em posts podem quebrar ao longo do tempo sem nenhuma detecção automática.
