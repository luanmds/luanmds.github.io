# Experiência com OpenCode + GitHub Copilot — Dados para Artigo

> Notas e métricas coletadas diretamente do banco de dados do OpenCode (`~/.local/share/opencode/opencode.db`) para uso no artigo bilíngue sobre a experiência de criar o blog com auxílio de um agente de código.

---

## Contexto do Projeto

- **Repositório:** `luanmds.github.io` — blog estático bilíngue (PT/EN) com Hugo + Congo
- **Hospedagem:** GitHub Pages em `https://luanmds.github.io/`
- **Ferramenta:** OpenCode com GitHub Copilot (assinatura flat fee — custo por token = $0)
- **Período:** 22 de abril a 6 de maio de 2026 (~2 semanas)

---

## Visão Geral

| Métrica | Valor |
|---|---|
| Total de sessões | 25 (14 principais + 11 subagent sessions) |
| Tempo ativo real | ~738 min (~12,3 horas) |
| **Tokens totais contabilizados** | **~141,7 milhões** |
| ↳ Cache reads (reutilizado) | ~134,2 milhões (94,7%) |
| ↳ Cache writes (gravado) | ~4,35 milhões (3,1%) |
| ↳ Output (gerado pelo modelo) | ~548 mil (0,4%) |
| ↳ Reasoning | ~308 mil (0,2%) |
| ↳ Input genuinamente novo | ~2,26 milhões (1,6%) |
| **Tokens realmente processados** | **~3,1 milhões** (input novo + output + reasoning) |
| Custo total | **$0,00** (GitHub Copilot) |
| Linhas adicionadas | +2.765 |
| Linhas removidas | -874 |
| Saldo líquido | +1.891 linhas |
| Arquivos modificados | 96 |

> **Sobre os 141,7 milhões de tokens:** A grande maioria (94,7%) são cache reads — o OpenCode envia o contexto completo da sessão (arquivos abertos, docs, histórico) a cada mensagem, mas o que já estava cacheado não é reprocessado pelo modelo. O consumo real de inferência foi de apenas ~3,1 milhões de tokens no total do projeto.

> **Nota sobre tempo ativo:** Duas sessões foram deixadas abertas por dias sem interação ("Tema Congo": 3,5 dias aberta; "Migração de artigos": 7 dias aberta). O tempo calculado acima exclui períodos idle (gaps > 30 min), representando apenas o tempo real de conversa ativa.

---

## Modelos LLM Utilizados

| Modelo | Sessões | Total contabilizado | Cache Read | Cache Write | Real processado |
|---|---|---|---|---|---|
| `gpt-5.3-codex` | 5 | ~90,2M | ~87,5M (96%) | — | **~2,7M** |
| `claude-sonnet-4.6` | 20 | ~47,9M | ~43,4M (90%) | ~4,1M | **~387K** |
| `claude-haiku-4.5` | 1 | ~4,9M | ~4,4M (91%) | ~368K | **~36K** |

> **Real processado** = input novo + output + reasoning — o que o modelo de fato inferiu.
> O `gpt-5.3-codex` concentra a maior parte do processamento real (~2,7M) por ter usado mais input novo e reasoning. O `claude-sonnet-4.6` usou apenas ~766 tokens de input novo em 20 sessões — praticamente todo o contexto já estava em cache.

---

## Breakdown de Tokens (Total Geral)

| Tipo | Quantidade | % do total |
|---|---|---|
| Cache reads | ~134,2 milhões | **94,7%** |
| Cache writes | ~4,35 milhões | 3,1% |
| Output (gerado pelo modelo) | ~548 mil | 0,4% |
| Reasoning | ~308 mil | 0,2% |
| Input genuinamente novo | ~2,26 milhões | 1,6% |

> O dado mais revelador: **94,7% dos tokens foram cache reads**. O OpenCode mantém o contexto completo (arquivos, docs, specs, histórico) em cache e o reutiliza a cada mensagem. Isso explica como 141 milhões de tokens são consumidos sem custo adicional em um plano flat.

---

## Sessões Principais — Detalhamento Completo

| Sessão | Tempo | ±Linhas | Total | Cache Read | Cache Write | Output | Input novo |
|---|---|---|---|---|---|---|---|
| Configure code automation in project | 14 min | +101/-2 | **1,5M** | 1,4M (93%) | — | 7K | 100K |
| Tema Congo e alternar idioma do artigo por link | 285 min | +904/-111 | **73,9M** | 72,0M (97%) | — | 99K | 1,8M |
| Coleta de contexto para documentação do projeto | 16 min | +804/-198 | **3,6M** | 3,2M (89%) | 335K | 30K | ~0 |
| Responsividade móvel, favicon e remover Tags | 33 min | +25/-16 | **5,7M** | 5,2M (91%) | 465K | 35K | ~0 |
| Migração de artigos e imagens do Medium/Google Drive | 166 min | +0/-0 | **23,2M** | 21,0M (91%) | 2,0M | 184K | ~0 |
| Ajustes finais no blog e padronização de specs | 39 min | +447/-214 | **5,9M** | 5,5M (94%) | — | 19K | 371K |
| Atualizar página Sobre: foto e trajetória profissional | 73 min | +36/-38 | **8,8M** | 8,5M (97%) | — | 21K | 279K |
| Congo theme colors and Spec 007 brainstorming | 71 min | +253/-229 | **10,6M** | 9,6M (91%) | 880K | 86K | ~0 |
| README.md com base em documentos e AGENTS.md | 32 min | +144/-16 | **7,1M** | 6,6M (93%) | 475K | 43K | ~0 |

### Resumo das Sessões Principais

Abaixo um resumo do contexto e do que foi efetivamente executado em cada uma dessas sessões principais listadas acima:

1. **Configure code automation in project**: Configuração das automações iniciais do projeto, como linting, CI/CD e configuração do CodeRabbit (QA sintético de Pull Requests).
2. **Tema Congo e alternar idioma do artigo por link**: Apesar do título no banco citar o tema Congo inicialmente, nesta sessão (a mais densa do projeto), foi configurada a base completa do blog com o Hugo, o tema inicial PaperMod e a estrutura completa de internacionalização (PT/EN) com chave de tradução nos artigos.
3. **Coleta de contexto para documentação do projeto**: Sessão dedicada a gerar a documentação base na pasta `.docs/`, mapeando stack, arquitetura, testes e estabelecendo o `AGENTS.md` a partir do estado atual do projeto.
4. **Responsividade móvel, favicon e remover Tags**: Ajustes finos de UI e UX, garantindo que o blog fosse responsivo, configurando o favicon correto e ajustando a exibição de tags nas postagens.
5. **Migração de artigos e imagens do Medium/Google Drive**: Uma sessão longa dedicada à migração de conteúdo em massa. O agente processou textos de rascunho (via Google Drive/Medium) e os formatou para markdown com front matter adequado, sem realizar commits diretos de engenharia.
6. **Ajustes finais no blog e padronização de specs**: Revisão geral de templates, padronização do formato dos artefatos dentro da pasta `specs/` (Spec-Driven Development) e refinamentos no blog antes do deploy.
7. **Atualizar página Sobre: foto e trajetória profissional**: Criação e atualização de conteúdo específico para a página *Sobre/About*, adicionando foto de perfil, histórico e ajustes de design específicos para essa rota.
8. **Congo theme colors and Spec 007 brainstorming**: Execução do Spec 007, que orquestrou 8 sub-agentes paralelos para migrar as cores e o layout do tema antigo (PaperMod) para o Congo, ajustando tipografia, paleta e estrutura de menus simultaneamente.
9. **README.md com base em documentos e AGENTS.md**: Geração do arquivo `README.md` público do repositório, extraindo todo o contexto do `AGENTS.md` e da documentação interna para apresentar o projeto.

**Legenda das colunas:**
- **Cache Read** — contexto reutilizado do cache (não reprocessado pelo modelo)
- **Cache Write** — contexto novo gravado no cache para reutilização futura
- **Output** — tokens gerados pelo modelo (respostas, código produzido)
- **Input novo** — tokens de entrada genuinamente novos naquela sessão

> **Observação sobre os modelos e cache:** Sessões com `gpt-5.3-codex` mostram Cache Write = 0 — esse modelo consome cache mas não registra escritas no mesmo formato do Claude. Sessões com `claude-sonnet-4.6` exibem o ciclo completo de leitura e escrita de cache.

---

## Skills do OpenCode Usadas por Sessão

A metodologia SDD (Spec-Driven Development) é visível na ordem consistente de uso das skills:

```
brainstorming → writing-plans → executing-plans → subagent-driven-development
```

| Sessão | Skills invocadas |
|---|---|
| List available skills | `writing-skills` |
| Tema Congo e alternar idioma do artigo por link | `brainstorming`, `writing-plans`, `executing-plans`, `using-git-worktrees`, `subagent-driven-development`, `test-driven-development`, `verification-before-completion`, `playwright-skill`, `systematic-debugging`, `finishing-a-development-branch`, `receiving-code-review` |
| Coleta de contexto para documentação do projeto | `brainstorming`, `writing-plans` |
| Responsividade móvel, favicon e remover Tags | `brainstorming`, `writing-plans` |
| Migração de artigos e imagens do Medium/Google Drive | `brainstorming`, `systematic-debugging`, `github-branch-pr`, `receiving-code-review` |
| Ajustes finais no blog e padronização de specs | `brainstorming`, `writing-plans`, `executing-plans`, `systematic-debugging`, `playwright-skill`, `github-branch-pr` |
| Atualizar página Sobre: foto e trajetória profissional | `brainstorming`, `writing-plans`, `executing-plans`, `using-git-worktrees`, `subagent-driven-development`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `github-branch-pr` |
| Congo theme colors and Spec 007 brainstorming | `brainstorming`, `writing-plans`, `subagent-driven-development` |
| README.md com base em documentos e AGENTS.md | `github-branch-pr` |

**Skills mais utilizadas (ranking):**

| Skill | Sessões |
|---|---|
| `brainstorming` | 8 |
| `writing-plans` | 6 |
| `github-branch-pr` | 3 |
| `executing-plans` | 3 |
| `subagent-driven-development` | 3 |
| `systematic-debugging` | 3 |
| `using-git-worktrees` | 2 |
| `test-driven-development` | 2 |
| `verification-before-completion` | 2 |
| `playwright-skill` | 2 |
| `receiving-code-review` | 2 |
| `finishing-a-development-branch` | 1 |
| `writing-skills` | 1 |

---

## Observações Notáveis

### 1. Custo zero percebido
141 milhões de tokens consumidos sem nenhum custo adicional. A assinatura do GitHub Copilot absorve tudo — não há billing por token.

### 2. Cache como viabilizador
94,7% dos tokens são cache reads. Em sessões Claude, o "Input novo" chega a valores próximos de zero (ex: `70`, `94`, `326` tokens por sessão inteira). O modelo literalmente só precisava processar uma frase nova por turno — todo o resto do contexto já estava cacheado.

### 3. Sessão gigante
"Tema Congo e alternar idioma do artigo por link" — 671 mensagens, 73,9M tokens, 904 linhas adicionadas, gerou a base do blog e o sistema de troca de idioma. Foi a sessão inaugural mais densa, com 1,8M tokens de input novo (contexto sendo apresentado pela primeira vez).

### 4. Padrão de subagents paralelos
Na sessão "Congo theme colors and Spec 007 brainstorming", 8 subagents foram lançados em paralelo para implementar, revisar e validar tarefas independentes de migração de tema. O padrão `dispatching-parallel-agents` → `subagent-driven-development` fica visível nos títulos das sessões filhas no banco de dados.

### 5. Migração com 0 linhas no git
A sessão "Migração de artigos e imagens do Medium/Google Drive" registrou 166 min de conversa ativa e 23,2M tokens, mas 0 linhas modificadas no repositório — imagens e conteúdo foram processados fora do controle de versão git.

### 6. SDD como estrutura observável
O fluxo Spec → Tasks → Implement é rastreável nos dados: sessões de brainstorming geram specs em `specs/`, sessões de execução consomem as tasks. O PR #8 (commits com `fix: address CodeRabbit`) passou por `receiving-code-review` após revisão automática do CodeRabbit.

### 7. Troca de modelos ao longo do projeto
O projeto começou com `gpt-5.3-codex`, migrou para `claude-sonnet-4.6` (padrão na maior parte do trabalho) e usou `claude-haiku-4.5` pontualmente no README. Cada modelo tem perfil diferente — Codex com mais tokens de reasoning, Claude com cache write explícito.

---

## Fonte dos Dados

Todos os dados foram extraídos diretamente de:
- `~/.local/share/opencode/opencode.db` — banco SQLite do OpenCode (tabelas: `session`, `message`, `part`)
- `git log` do repositório `luanmds.github.io`

Script de extração executado em: **06 de maio de 2026**
