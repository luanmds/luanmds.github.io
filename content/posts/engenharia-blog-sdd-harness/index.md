---
title: "A Engenharia por trás deste blog: SDD e Harness em um workflow 100% IA"
date: 2026-05-09
draft: true
tags: ["engenharia-de-software", "inteligencia-artificial", "sdd", "harness-engineering"]
categories: ["Engenharia"]
summary: "Um relato técnico sobre como este blog foi construído utilizando desenvolvimento assistido por IA, validando os limites de SDD e Harness Engineering."
cover:
  image: cover.png
  alt: "Capa representando o ciclo de vida SDD assistido por IA"
  relative: true
translationKey: "engenharia-blog-sdd-harness"
---

Esse artigo consolida todo o processo e conhecimento adquirido com o projeto como **AI-Driven** desde a escolha do framework base do blog até o deploy no Github Pages.

## Motivação e Contexto do Experimento

Após passar as últimas semanas me aprofundando e entendendo os conceitos de **Spec-Driven Development (SDD)** e, principalmente, **Harness Engineering**. Decidi colocar em prática com um pequeno projeto - chamado também de *brownfield* - que estava engavetado: _meu próprio blog_.

Além disso, a ideia da prática partiu inicialmente do artigo do mestre Fábio Akita ([aqui](https://akitaonrails.com/2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles/#o-claudemd-a-spec-que-evolui)), no qual ele demonstra o uso da IA como assistente em um projeto real, contendo detalhes da implementação. E o projeto foi incrementado com docs do artigo do Eugênio (Gnios) com dicas de como podemos documentar contexto sobre o projeto para uso das IAs ([aqui](https://gnios.github.io/blog/documentacao-antes-das-ferramentas/)).

Em resumo, esse projeto valida a tese sobre **como é usar uma IA como assistente no dia a dia**. A seguir, trago como foi discutir ideias através de brainstormings, montar specs com um fluxo personalizado bem simples de SDD e ajustar instruções para os agentes através do feedback dela mesma usando princípios do Harness Engineering. Sem enrolacão, bora lá!

## Tooling, Stack & Harness Customizado do Projeto

- **Stack:** HuGo + Tema Congo (decisões via brainstorming-skill).
  - Migração do Tema PaperMod para o Congo
- **O Harness Customizado:**
  - AGENTS.md: A "Constituição" do projeto e o manual de bordo para os agentes.
  - Pasta .docs/: Engenharia de Contexto como fonte da verdade.
  - **CodeRabbit:** Portão de qualidade (QA sintético) para revisão de PRs.

Antes de mergulharmos na metodologia e suas métricas, vamos destrinchar as tecnologias base e o harness customizado do projeto.

### Stack utilizada

- `Framework HuGo`: Para **construção do corpo do site **e o tema [Congo](https://themes.gohugo.io/themes/congo) com cores customizadas.
- `Github Pages e Github Actions`: para **hospedar e realizar deploy**, respectivamente. Tudo de forma gratuita do próprio Github. 
  - Para saber mais verifique essa [doc deles](https://docs.github.com/en/pages).
- `CodeRabbit AI`: Agente QA sintético - com free tier! - para **revisar o código gerado em Pull Requests abertos por outros agentes** no repositório. 
  - Configurado através do arquivo `.coderabbit.yaml`
- `Playwright via Docker`: Ferramenta para automatizar testes funcionais em páginas web. No projeto, tem o **papel de validar uma alteracão no front-end** antes de seguir com commit e merge.

### Harness Feedforward

- `AGENTS.md`: principal arquivo com todo o resumo do projeto e um manual de bordo para os agentes seguirem o workflow configurado para o projeto.
- `.docs/`: pasta com informações detalhadas do contexto relacionado ao projeto. Possui todas as diretivas e cada arquivo é mapeado no `AGENTS.md`.
- `specs/`: pasta com as especificações desenvolvidas e implementadas. Cada especificação possui um arquivo `tasks.md` onde é listado tudo o que deve ser feito para que consideremos a implementação como Done.

![print dos arquivos e pastas no projeto]()

## A Metodologia Spec-Driven e Orquestracão de Agentes

- **Spec-Driven Development (SDD):** Por que a especificação (specs/) precede o código.
- **Ciclo de Vida:** *Spec -> Tasks -> Implement*.
- **Subagent-Driven Development:** O caso da **Spec 007** (Congo Migration) com 8 subagentes paralelos coordenados.

O **Spec-Driven Development (SDD)** foi o pilar da produtividade. Diferente do modelo tradicional onde o código é o artefato principal, aqui a especificação (Spec) torna-se o contrato que guia todo o downstream.

### O Ciclo de Vida da Entrega

O fluxo de trabalho foi dividido em etapas claras e interdependentes:

- **Brainstorming:** Uso da brainstorming-skill para validar decisões arquiteturais e de stack antes do primeiro commit.
- **Especificação (Spec):** Criação de arquivos Markdown na pasta specs/ detalhando o comportamento esperado e as restrições técnicas.
- **Decomposição em Tarefas:** Tradução da Spec para um tasks.md com itens atômicos, paralelizáveis e com *Definition of Done* (DoD) bem definida.
- **Implementação:** Onde os agentes de IA executavam as tarefas sob a supervisão do *Harness*.

### Orquestração: O Caso Spec 007

O teste de fogo foi a **Spec 007 (Migração para o tema Congo)**. Em vez de uma execução linear, apliquei o **Subagent-Driven Development**: o agente orquestrador disparou **8 sub-agentes paralelos**. Cada sub-agente assumiu um domínio específico (cores, tipografia, estrutura de menus), todos operando simultaneamente sobre a mesma fonte da verdade (a Spec). Isso permitiu uma migração complexa em tempo recorde, com consistência arquitetural garantida.


## Análise de Métricas do OpenCode 

Dados extraídos do banco de dados do OpenCode (opencode.db) cobrindo o período de 22 de abril a 6 de maio de 2026.

| Métrica | Valor | |---|---| | Total de Tokens Processados | ~141,7 milhões | | **Cache Reads (Eficiência de Contexto)** | ~134,2 milhões (**94,7%**) | | Cache Writes | ~4,35 milhões (3,1%) | | Output (Gerado pelo modelo) | ~548 mil (0,4%) | | Input Novo | ~2,26 milhões (1,6%) | | Tempo Ativo Real | ~738 min (~12,3 horas) | | Saldo Líquido de Código | +1.891 linhas (96 arquivos) |

**Análise Técnica:** A taxa de **94,7% de Cache Reads** demonstra o sucesso do *Context Engineering*. Ao manter o contexto "quente" e estável, o agente pôde operar com máxima precisão, reduzindo alucinações. O fato de apenas 0,4% do processamento ter resultado em saída gerada prova que o valor real da IA está no **raciocínio sobre o contexto existente** para garantir que as 1.891 linhas líquidas de código fossem tecnicamente perfeitas.

![Token Usage](tokens.png)

Extras:

- **Sobre os 141,7 milhões de tokens:** A grande maioria (94,7%) são cache reads — o OpenCode envia o contexto completo da sessão (arquivos abertos, docs, histórico) a cada mensagem, mas o que já estava cacheado não é reprocessado pelo modelo. O consumo real de inferência foi de apenas ~3,1 milhões de tokens no total do projeto
- Trazer linhas de código escritas em cada sessão

### Rascunho

## Conclusões e Lições Aprendidas

- Mudança de mindset: O desenvolvedor sênior como "Designer de Contexto" e "Orquestrador de Agentes".
- A suficiência do AGENTS.md para projetos de escala média vs. frameworks complexos.
- Próximos passos e aplicação em ambientes corporativos.

## Referências

### SDD e Context Engineering

- [Spec-Driven Development: AI Assisted Coding Explained](https://youtu.be/mViFYTwWvcM?si=7xuFcJLoD_18k71L)
- [Spec-Driven Development: A Habilidade #1 para Devs de 2026 (Guia Completo)](https://www.youtube.com/watch?v=YFDp-smGYqQ)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl — Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [The ONLY guide you'll need for GitHub Spec Kit](https://www.youtube.com/watch?v=a9eR1xsfvHg)
- [Diving Into Spec-Driven Development With GitHub Spec Kit — Microsoft for Developers](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)

### AI-Assisted Development

- [AI-Assisted Coding Tutorial – OpenClaw, GitHub Copilot, Claude Code, CodeRabbit, Gemini CLI](https://www.youtube.com/watch?v=wlpBCazAY9Q)
- [Do Zero à Pós-Produção em 1 Semana — Fábio Akita](https://akitaonrails.com/2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles/#o-claudemd-a-spec-que-evolui)
- [O Método Fábio Akita para programar com IA](https://youtu.be/cWY7iBafw7I?t=2301)
- [Antes de qualquer ferramenta: como documentar seu projeto para a IA — Gnios](https://gnios.github.io/blog/documentacao-antes-das-ferramentas/)
- [How do thinking and reasoning models work?](https://www.youtube.com/watch?v=xCRvOUykOX0)
- [Large Language Models Survey — arxiv.org](https://arxiv.org/pdf/2601.20245)
