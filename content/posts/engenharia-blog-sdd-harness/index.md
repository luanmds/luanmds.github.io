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

Além disso, a ideia da prática partiu inicialmente do artigo do mestre _Fábio Akita_ ([aqui](https://akitaonrails.com/2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles/#o-claudemd-a-spec-que-evolui)), no qual ele demonstra o uso da IA como assistente em um projeto real, contendo detalhes da implementação. E o projeto foi incrementado com docs do artigo do _Eugênio (Gnios)_ com dicas de como podemos documentar contexto sobre o projeto para uso das IAs ([aqui](https://gnios.github.io/blog/documentacao-antes-das-ferramentas/)).

Em resumo, esse projeto valida a tese sobre **como é usar uma IA como assistente no dia a dia**. A seguir, trago como foi discutir ideias através de brainstormings, montar specs com um fluxo personalizado bem simples de SDD e ajustar instruções para os agentes através do feedback dela mesma usando princípios do Harness Engineering. Sem enrolacão, bora lá!

## Tooling, Stack & Harness Customizado do Projeto

Antes de mergulharmos na metodologia e suas métricas, vamos destrinchar as tecnologias base e o harness customizado do projeto.

### Stack utilizada

- `HuGo Framework`: Para **construção do corpo do site** e o tema [Congo](https://themes.gohugo.io/themes/congo) com cores customizadas.
- `Github Pages e Github Actions`: para **hospedar e realizar deploy**, respectivamente. Tudo de forma gratuita do próprio Github. 
  - Para saber mais verifique essa [documentação deles](https://docs.github.com/en/pages).
- `CodeRabbit`: AI Agent QA sintético - com free tier! - para **revisar o código gerado em Pull Requests abertos por outros agentes** no repositório. 
  - Configurado através do arquivo `.coderabbit.yaml`
- `Playwright`: Ferramenta/Library utilizada para automatizar testes funcionais em páginas web. No projeto, tem o **papel de validar alterações no front-end** antes de seguir com commit e merge.
- `OpenCode`: AI Agent via terminal, com foco em **codificação e uso de ferramentas**. Utilizado como parceiro de codificação principal. A maior vantagem é a capacidade de usar diversos modelos LLM e suas skills.
  - É orquestrado pelo harness do projeto para seguir o workflow SDD.
  - Por ser agnóstico a modelos, foi possível testar com diferentes LLMs diferentes, como *Claude Sonnet*, *Claude Haiku* e *GPT-5.3 Codex*.

### Harness Feedforward

- `AGENTS.md`: principal arquivo com todo o resumo do projeto e um manual de bordo para os agentes seguirem o workflow configurado para o projeto.
- `.docs/`: pasta com informações detalhadas do contexto relacionado ao projeto. Possui todas as diretivas e cada arquivo é mapeado no `AGENTS.md`.
- `specs/`: pasta com as especificações desenvolvidas e implementadas. Cada especificação possui um arquivo `tasks.md` onde é listado tudo o que deve ser feito para que consideremos a implementação como Done.

Abaixo, um print de como ficou o harness organizado no projeto:

![estrutura de pastas do harness](./project_structure.png)

## A Metodologia Spec-Driven e Orquestracão de Agentes

Algo que aprendi estudando o Harness é que **entender melhor o ciclo de vida é fundamental para o alinhamento inicial** e, principalmente, o que pode ou não ser feito. 

No Spec-Driven Development, **a especificação é o pilar que guia todo o processo de criação de conteúdo**. Iniciando por um _brainstorming_, passando por uma etapa de especificação, decomposição em tarefas e implementação. Aqui percebi que **a especificacão se torna o artefato principal desse processo**, diferente do desenvolvimento tradicional onde o código é o artefato principal.

### O Ciclo de Vida da Entrega

O fluxo de trabalho foi dividido em etapas claras e interdependentes:

#### 1. Planejamento

- **Brainstorming:** Uso da `brainstorming-skill` (do [Superpowers Skills](https://github.com/obra/superpowers)) para validar decisões arquiteturais e de stack antes do primeiro commit.
- **Especificação (Spec):** Criação de arquivos Markdown na pasta `specs/` (operando em modo *PLAN*) detalhando o comportamento esperado e as restrições técnicas.
- **Validação do Usuário:** Etapa obrigatória (*Verify and Validate*) onde a especificação é revisada, refinada e aprovada pelo "Product Owner" (o próprio usuário) antes de qualquer código ser gerado.

#### 2. Execução

- **Decomposição em Tarefas:** Tradução da Spec aprovada para um arquivo `tasks.md` com itens atômicos, paralelizáveis e com *Definition of Done* (DoD) bem definida.
- **Implementação:** Fase onde os agentes de IA assumem a execução das tarefas e escrevem o código sob a supervisão restrita do *Harness*.
- **Testes com Playwright:** Validação visual e funcional da entrega utilizando a `playwright-skill` rodando localmente (via Docker) antes de seguir para o commit.

#### 3. Qualidade e Deploy

- **Pull Request e CodeRabbit:** Empacotamento das mudanças em um PR, engatilhando a revisão de código automatizada do CodeRabbit AI.
- **Deploy Contínuo:** Publicação automatizada via GitHub Actions enviando a versão validada para o GitHub Pages.

{{< mermaid >}}
flowchart TD
    %% Phase 1
    subgraph Planning
        direction LR
        B[Brainstorming Skill] --> S[Spec Creation]
        S --> V{User Validation}
        V -- Refine --> S
    end

    %% Phase 2
    subgraph Execution
        direction LR
        T[Task Decomposition] --> I[Implementation]
        I --> P[Playwright Tests]
        P -- Fail --> I
    end

    %% Phase 3
    subgraph QD[Quality & Deploy]
        direction LR
        PR[Create Pull Request] --> CR[CodeRabbit AI Review]
        CR -- Issues Resolved --> D[Deploy to GH Pages]
    end

    Planning -- Approved --> Execution
    Execution -- Pass --> QD
{{< /mermaid >}}

### Casos de Uso em Destaque

Durante o tempo do experimento, alguns cenários destacaram, na prática, o potencial e a flexibilidade dessa abordagem.

#### 1. A Sessão Gigante: Construindo a Base (Tema PaperMod + Multilingual)
Esta foi a sessão inaugural e a mais densa de todo o projeto. Com duração de **285 minutos** de tempo ativo real e 671 mensagens trocadas, o agente foi responsável por gerar a base completa do tema PaperMod no blog e todo o sistema de troca de idioma. 
O mais impressionante foram os números: **~73,9 milhões de tokens** foram consumidos nesta única sessão, resultando em um saldo de **+904 linhas de código** adicionadas. Desse total de tokens, incríveis 97% foram lidos diretamente do cache do contexto já estabelecido.

#### 2. Spec 007: Migração do tema PaperMod para Congo com Subagents Paralelos
Um outro caso notável foi a especificação **Spec 007 (Migração do tema PaperMod para Congo)**. O trabalho durou **71 minutos**, com uma alteração concentrada de +253 linhas e remoção de 229 linhas, e um consumo total de **~10,6 milhões de tokens**.

Em vez de uma execução linear, apliquei o padrão **Subagent-Driven Development**: o agente orquestrador disparou **8 sub-agentes paralelos**. Cada sub-agente assumiu uma tarefa independente (cores, tipografia, estrutura de menus), todos operando simultaneamente sobre a mesma fonte da verdade (a Spec). Isso permitiu uma migração complexa em tempo recorde, com consistência arquitetural garantida.

## Análise de Métricas do OpenCode 

Os dados abaixo foram extraídos diretamente do banco de dados do OpenCode (via arquivo `opencode.db`) cobrindo o período do projeto. No total, tivemos **25 sessões** (~12,3 horas de tempo ativo real), que modificaram 96 arquivos e geraram um saldo líquido de +1.891 linhas de código (+2.765 adicionadas, -874 removidas).

Abaixo o detalhamento das métricas de processamento:

| Métrica | Quantidade | % do total |
|---|---|---|
| **Total de Tokens Contabilizados** | **~141,7 milhões** | **100%** |
| Cache Reads (reutilizado) | ~134,2 milhões | 94,7% |
| Cache Writes (gravado) | ~4,35 milhões | 3,1% |
| Output (gerado pelo modelo) | ~548 mil | 0,4% |
| Reasoning (raciocínio oculto) | ~308 mil | 0,2% |
| Input genuinamente novo | ~2,26 milhões | 1,6% |

**A Mágica do Cache e Custo Zero**
O dado mais revelador do experimento: **94,7% dos tokens foram lidos do cache** (Context Efficiency). O agente mantém o contexto completo "quente" (arquivos, documentação, histórico) a cada mensagem enviada, mas o modelo não precisa reprocessar o que já está cacheado. 

Isso explica como foi possível consumir **141,7 milhões de tokens sem custo adicional** usando a assinatura do GitHub Copilot. O consumo real de inferência (input novo + reasoning + output) foi de apenas ~3,1 milhões de tokens.

**Sessões Principais e Produtividade**
A tabela abaixo mostra a distribuição de esforço e saldo de código nas principais sessões do projeto:

| Sessão (Foco) | Tempo Ativo | Saldo de Linhas | Tokens Totais |
|---|---|---|---|
| Project Base (HuGo + PaperMod + Multilingual) | 285 min | +904 / -111 | 73,9M |
| Migração de artigos (arquivos `.doc` no Google Drive) | 166 min | +0 / -0 | 23,2M |
| Atualizar página Sobre/About | 73 min | +36 / -38 | 8,8M |
| Migração Tema Congo (Spec 007) | 71 min | +253 / -229 | 10,6M |
| Ajustes finais + update de specs | 39 min | +447 / -214 | 5,9M |
| Responsividade/favicon/Tags | 33 min | +25 / -16 | 5,7M |
| README.md | 32 min | +144 / -16 | 7,1M |
| Coleta de contexto | 16 min | +804 / -198 | 3,6M |
| Configure code automation | 14 min | +101 / -2 | 1,5M |

> *Observação: A sessão de "Migração de artigos" levou 166 minutos e processou 23 milhões de tokens sem modificar nenhuma linha de código no repositório final. Isso ocorreu pois o conteúdo e as imagens foram processados fora do controle de versão (geração de conteúdo bruto em massa).*

**Resumo das Atividades por Sessão:**
- **Project Base**: Sessão mais densa. O agente configurou a base completa do blog com o Hugo, o tema inicial PaperMod e a infraestrutura de internacionalização (PT/EN) com chave de tradução.
- **Migração de artigos**: Sessão longa focada em processar textos de rascunho (via Google Drive/Medium) e formatá-los para markdown com front matter adequado.
- **Atualizar página Sobre/About**: Criação e atualização de conteúdo específico para a página *Sobre/About*, como foto de perfil, histórico e ajustes de design pontuais.
- **Migração Tema Congo (Spec 007)**: Execução da Spec 007, orquestrando 8 sub-agentes paralelos para migrar as cores e layout do tema antigo para o Congo, ajustando tipografia e menus simultaneamente.
- **Ajustes finais + update de specs**: Revisão de templates, padronização do formato dos artefatos na pasta `specs/` e refinamentos antes do deploy final.
- **Responsividade/favicon/Tags**: Ajustes finos de UI/UX, garantindo navegação responsiva, o favicon correto e a exibição de tags nas postagens.
- **README.md**: Geração do arquivo público do repositório, extraindo o contexto diretamente da documentação interna.
- **Coleta de contexto**: Sessão dedicada a gerar a documentação base na pasta `.docs/`, mapeando stack, arquitetura e estabelecendo o `AGENTS.md` a partir do estado atual.
- **Configure code automation**: Configuração inicial de linting, CI/CD e integração do CodeRabbit (QA sintético de Pull Requests).

### Modelos LLM Utilizados nas sessões principais

| Modelo | Sessões | Total contabilizado | Cache Read | Cache Write | Real processado |
|---|---|---|---|---|---|
| `gpt-5.3-codex` | 5 | ~90,2M | ~87,5M (96%) | — | **~2,7M** |
| `claude-sonnet-4.6` | 20 | ~47,9M | ~43,4M (90%) | ~4,1M | **~387K** |
| `claude-haiku-4.5` | 1 | ~4,9M | ~4,4M (91%) | ~368K | **~36K** |

> ***Observação**: Real processado = input novo + output + reasoning — o que o modelo de fato inferiu.*

## Conclusão

Após colocar a versão 1.0 do projeto em produção ([https://luanmds.github.io](https://luanmds.github.io)), listei algumas conclusões e lições aprendidas ao longo do processo:

- **Mudança de mindset como Dev**: O desenvolvedor passa a ser um "Designer de Contexto" e "Orquestrador de Agentes". O que não é ruim - no meu ponto de vista - mas exige um aprendizado de como interagir com as IAs para extrair o máximo de benefício. **Mas ainda é preciso entender o que a IA está gerando e ter um conhecimento sólido sobre Arquitetura e Design de Software** para garantir que o software mantenha um nível de qualidade aceitável.

- **Documentacão é a chave para uma boa experiência**: À medida que a GenAI avança, a capacidade de interagir com ela de forma eficaz se torna uma habilidade crítica. **A qualidade da documentação influencia diretamente a capacidade da IA de entender o contexto do projeto** e gerar respostas relevantes e precisas.
  - A importância do `AGENTS.md` como artefato central de documentação, ou seja, um guia que o Agente sempre levar consigo ao interagirmos com ele.
  - O SDD, independente de usar um framework ou ferramenta específica (como o OpenCode), se mostra a melhor forma de documentar um projeto. Isso porque ele se baseia no conceito de *"documentação do que precisa ser feito"* ao invés de *"documentação do que foi feito"*.


- **Processo de Harness é o mais importante no processo de uso da IA como assistente**: Sem ele, a IA tem dificuldade em entender o contexto do projeto e gerar respostas relevantes e precisas. Por isso, é importante estar sempre revisando o input usado pela IA (Feedforward) e o que ela retorna como resposta (Feedback) para que consiga refinar o contexto do projeto. 

>Parafraseando o mestre Fábio Akita: *"Faça um bom prompt, teste, veja o que ele retornou. Se não ficou bom, conserte seu prompt e refaça"*.

## Referências

### SDD, Harness Engineering & Context Engineering

- [Spec-Driven Development: AI Assisted Coding Explained](https://youtu.be/mViFYTwWvcM?si=7xuFcJLoD_18k71L)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl — Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [The ONLY guide you'll need for GitHub Spec Kit](https://www.youtube.com/watch?v=a9eR1xsfvHg)

### AI-Assisted Development

- [AI-Assisted Coding Tutorial – OpenClaw, GitHub Copilot, Claude Code, CodeRabbit, Gemini CLI](https://www.youtube.com/watch?v=wlpBCazAY9Q)
- [Do Zero à Pós-Produção em 1 Semana — Fábio Akita](https://akitaonrails.com/2026/02/20/do-zero-a-pos-producao-em-1-semana-como-usar-ia-em-projetos-de-verdade-bastidores-do-the-m-akita-chronicles/#o-claudemd-a-spec-que-evolui)
- [Antes de qualquer ferramenta: como documentar seu projeto para a IA — Gnios](https://gnios.github.io/blog/documentacao-antes-das-ferramentas/)
- [How do thinking and reasoning models work?](https://www.youtube.com/watch?v=xCRvOUykOX0)
- [Large Language Models Survey — arxiv.org](https://arxiv.org/pdf/2601.20245)
