---
title: "The Engineering behind this blog: SDD and Harness in a 100% AI workflow"
date: 2026-05-08
draft: true
tags: ["software-engineering", "artificial-intelligence", "sdd", "harness-engineering", "hugo"]
categories: ["Engineering"]
summary: "A technical report on how this blog was built using AI-assisted development, validating the limits of SDD and Harness Engineering."
cover:
  image: cover.png
  alt: "AI-assisted SDD lifecycle diagram"
  relative: true
translationKey: "engenharia-blog-sdd-harness"
---

# Engineering Lab: Validating SDD and Harness Engineering in a 100% AI-assisted workflow

This document serves as the base structure for the technical article detailing the experiment of building the blog **luanmds.github.io** using advanced AI-assisted engineering methodologies.

## I. Experiment Context

- **Motivation:** Report of a practical study to validate the limits of assisted development.
- **Inspiration:** Reference to the works of Akita (AI use in real projects) and Eugênio/Gnios (context documentation).
- **The Thesis:** Validation of maintaining technical rigor (clean code, architecture) using AI agents without heavy SDD frameworks, focusing on customized "Harness Engineering".

### Draft

This article consolidates the entire process and knowledge acquired with the project as AI-Driven from the choice of the blog's base framework to the deployment on Github Pages.

After spending the last few weeks studying and understanding the concepts of Spec-Driven Development (SDD) and, especially, Harness Engineering. I decided to put into practice with a small project - also called brownfield - that was shelved: my own blog.

In addition, the idea for the practice initially came from the article by master Fábio Akita (link), in which he demonstrates the use of AI as an assistant in a real project, containing implementation details. And the project was incremented with docs from Eugênio's (Gnios) article with tips for creating docs about the project (link).

In summary, this project validates and brings important points about what it's like to use an AI as an assistant in daily life, discussing ideas through brainstorming, setting up specs with a customized and very simple SDD workflow and adjusting instructions for agents through their own feedback, using the principles of Harness Engineering.

## II. Lab Setup (Tooling & Harness)

- **Stack:** HuGo + Congo Theme (decisions via brainstorming-skill).
  - Migration from PaperMod Theme to Congo
- **The Customized Harness:**
  - AGENTS.md: The "Constitution" of the project and the onboard manual for agents.
  - .docs/ folder: Context Engineering as the source of truth.
  - **CodeRabbit:** Quality gate (synthetic QA) for PR reviews.

### Draft

Title: Technologies and standards used

Before we dive into the methodology and its metrics, let's break down the base technologies and the customized harness of the project.

Stack used:

- HuGo framework for building the site body and the Congo theme with customized colors.
- Github Pages and Github Actions for hosting and deploying, respectively. All for free from Github itself. To find out more check their doc:
- CodeRabbit AI: Free tier agent to review code generated in Pull Requests opened by other agents in the repository.

Feedforward Harness:

- AGENTS.md: main file with the entire project summary and an onboard manual for agents to follow the workflow configured for the project.
- .docs/: folder with detailed information on the context related to the project. It has all the directives and each file is mapped in [AGENTS.md](http://agents.md) so that the agent can read it when necessary.
- specs/: folder with developed and implemented specifications. Each specification has a [tasks.md](http://tasks.md) file where everything that must be done for us to consider the implementation as Done is listed.

(screenshot of files and folders in the project)

## III. The Methodology: SDD and Agent Orchestration

- **Spec-Driven Development (SDD):** Why the specification (specs/) precedes the code.
- **Lifecycle:** *Spec -> Tasks -> Implement*.
- **Subagent-Driven Development:** The case of **Spec 007** (Congo Migration) with 8 parallel agents coordinated.

### Draft

Title: Spec-Driven and Agent Orchestration

**Spec-Driven Development (SDD)** was the pillar of productivity. Unlike the traditional model where code is the main artifact, here the specification (Spec) becomes the contract that guides all downstream.

### Delivery Lifecycle

The workflow was divided into clear and interdependent stages:

- **Brainstorming:** Use of the brainstorming-skill to validate architectural and stack decisions before the first commit.
- **Specification (Spec):** Creation of Markdown files in the specs/ folder detailing expected behavior and technical constraints.
- **Decomposition into Tasks:** Translation of the Spec into a tasks.md with atomic, parallelizable items and a well-defined *Definition of Done* (DoD).
- **Implementation:** Where AI agents executed tasks under the supervision of the *Harness*.

### Orchestration: The Spec 007 Case

The fire test was **Spec 007 (Migration to Congo theme)**. Instead of a linear execution, I applied **Subagent-Driven Development**: the orchestrator agent fired **8 parallel sub-agents**. Each sub-agent took over a specific domain (colors, typography, menu structure), all operating simultaneously on the same source of truth (the Spec). This allowed for a complex migration in record time, with guaranteed architectural consistency.

![SDD Lifecycle](lifecycle.png)

## IV. Data Analysis (OpenCode Metrics)

Data extracted from the OpenCode database (opencode.db) covering the period from April 22nd to May 6th, 2026.

| Metric | Value | |---|---| | Total Processed Tokens | ~141.7 million | | **Cache Reads (Context Efficiency)** | ~134.2 million (**94.7%**) | | Cache Writes | ~4.35 million (3.1%) | | Output (Generated by the model) | ~548 thousand (0.4%) | | New Input | ~2.26 million (1.6%) | | Real Active Time | ~738 min (~12.3 hours) | | Net Code Balance | +1,891 lines (96 files) |

**Technical Analysis:** The **94.7% Cache Reads** rate demonstrates the success of *Context Engineering*. By keeping the context "hot" and stable, the agent was able to operate with maximum precision, reducing hallucinations. The fact that only 0.4% of processing resulted in generated output proves that the real value of AI lies in **reasoning over existing context** to ensure that the 1,891 net lines of code were technically perfect.

![Token Usage](tokens.png)

Extras:

- **About the 141.7 million tokens:** The vast majority (94.7%) are cache reads — OpenCode sends the full session context (open files, docs, history) with each message, but what was already cached is not reprocessed by the model. The real inference consumption was only ~3.1 million tokens in the entire project.
- Bring lines of code written in each session

### Draft

## V. Conclusions and Lessons Learned

- Mindset change: The senior developer as "Context Designer" and "Agent Orchestrator".
- The sufficiency of AGENTS.md for medium-scale projects vs. complex frameworks.
- Next steps and application in corporate environments.
