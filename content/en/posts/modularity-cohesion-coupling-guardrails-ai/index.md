---
title: "Keeping Modularity, Cohesion and Coupling with Guardrails in the AI Era"
date: 2026-09-01
draft: false
tags: ["software-architecture", "artificial-intelligence", "modularity", "cohesion", "coupling"]
categories: ["software-architecture"]
summary: "Exploration of the principles and applicability of modularity, cohesion, and coupling in software architecture, especially in the context of artificial intelligence."
cover:
  image: cover.png
  alt: "Representing the concepts of modularity, cohesion and coupling in a software"
  relative: true
translationKey: "modularity-cohesion-coupling-guardrails-ai"
---

With the advent of Artificial Intelligence (AI), you've probably already realised - and seen in many places - that AI has become a commodity kind, with the ability to generate code quickly and at scale. However, this doesn't guarantee the quality and security of the software being developed and creates difficulties in maintaining and sustaining the system in the long term.

In this article, we will revisit some essential software engineering fundamentals that have always served as guardrails for the design and architecture of our software, and understand why it's essential to apply them today, particularly when we incorporate AI as a partner in the maintenance and development of the software lifecycle.


## Revisiting Modularity, Cohesion and Coupling

Next, we will review the concepts of modularity, cohesion, and coupling, understanding how they relate to each other and how they impact software quality in the long term. This allows us to make decisions based on technical and business trade-offs.

### Modularity and Granularity for Organizing Responsibilities

In short, **modularity** is a general term to indicate any grouping of code: classes (in object-oriented programming), functions (in functional paradigms), libraries, services, etc. Its main focus is to divide the system into parts (groupings) that facilitate understanding, while being independent and cohesive (we'll see about cohesion next). Each part is generally called a **module**.

It's greatest advantage lies precisely in this modular division, as it makes it easier to maintain and evolve the software, allowing to identity which code, or in which modules, should be changed to address a new requirement or bug fix.
    
#### Module Granularity

While modularity focuses on grouping code according to responsibilities, **the granularity focuses on the size of the module**, meaning a module can contain one or more responsabilities.

And the definition of how granular a module should be is a part of the chosen architecture style: a monolithic architecture can have modules following business rules (example 1 below) or separated by technical parts, as in layered architecture. A microservices architecture tends to have smaller modules, with more specific responsibilities focused on business domains (example 2 below).

> **Tip**: Think of granularity as a *trade-off* that comes with the architecture chosen for the system and constantly reevaluate it for each module. As the system evolves, a module's responsibilities may change, and be ready to split it into a new service.
    
Here are some examples of modularity:

*Example 1: Modular monolith with well-defined boundaries.*

{{< mermaid >}}
flowchart TD
    UI[Web Interface] --> App[Application Layer]
    App --> Auth[Auth Module]
    App --> Catalog[Catalog Module]
    App --> Order[Order Module]
    Catalog --> Shared[Shared Kernel]
    Order --> Shared[Shared Kernel]
    Auth --> DB[(Single Database)]
    Catalog --> DB
    Order --> DB
{{< /mermaid >}}

*Example 2: Modules in a microservices architecture.*

{{< mermaid >}}
flowchart LR
    Client[Client] --> Gateway[API Gateway]
    Gateway --> CatalogSvc[Catalog Service]
    Gateway --> OrderSvc[Order Service]
    Gateway --> NotifSvc[Notification Service]
    CatalogSvc --> CatalogDB[(Catalog DB)]
    OrderSvc --> OrderDB[(Order DB)]
    NotifSvc --> NotifDB[(Notification DB)]
{{< /mermaid >}}


### Cohesion for Creating Meaning Among Parts

Serving as a quality metric, cohesion indicates how well the parts of a module are related to each other, fulfilling the responsibility assigned to it. While the modularity groups, the cohesion ensures that the grouping makes sense.

In an ideal scenario, a module considered "cohesive" contains everything essential for its operation, without depending on other modules to fulfill its responsibility. Trying to add more actions or to split it can result in increased coupling (we'll see next) and loss of readability. In the end, the cohesion is a question too: *"What does this module do or is doing? Does it fulfill the responsibility assigned to it?"*

#### And how to define the responsibility?

The responsibility is defined by the function that the module must fulfill within the system. Whether by a domain or subdomain defined using Domain-Driven Design (DDD), by a business rule, or by a shared technical functionality (such as an authentication service, for example).

> **Tip**: Get into the habit of naming modules based on the responsibility they fulfill, this helps maintain cohesion and facilitates system understanding. Always review what the module does and if what is in it still fulfills the responsibility assigned to it. If not, it's time to refactor.


#### Types of Cohesion

There are several types of cohesion, but the most commons and the ones we should focus on are:

- **Functional Cohesion**: All parts of the module work together to perform a single well-defined function. This is the ideal case of a module. **Example**: An authentication module that handles login, logout, and token verification.
- **Coincidental Cohesion**: The parts of the module are grouped together, but they do not have a clear relationship with each other. **Example**: A module that contains authentication functions, file handling, and email sending.
- Other types of cohesion include **Logical Cohesion**, **Temporal Cohesion**, **Procedural Cohesion**, among others, each with its characteristics and impacts on software quality. *I recommend reading the article [Cohesion and Coupling](https://www.geeksforgeeks.org/software-engineering/software-engineering-coupling-and-cohesion/) for a more detailed view.*

Some use cases of cohesion:

*Example 1: High cohesion in an authentication module.*

{{< mermaid >}}
flowchart TD
    UI[Login Screen] --> Auth[Authentication Module]
    Auth --> Validate[Validate Credentials]
    Auth --> Token[Issue JWT Token]
    Auth --> Refresh[Refresh Session]
    Validate --> UserDB[(Users Database)]
    Token --> TokenStore[(Token Store)]
    Refresh --> TokenStore
{{< /mermaid >}}

*Example 2: Low cohesion mixing different responsibilities.*

{{< mermaid >}}
flowchart TD
    UI[Admin Panel] --> Mixed[Mixed Module]
    Mixed --> Order[Create Order]
    Mixed --> Payment[Process Payment]
    Mixed --> Email[Send Email]
    Mixed --> Report[Generate Report]
    Order --> OrderDB[(Orders DB)]
    Payment --> PayDB[(Payments DB)]
    Email --> MailSvc[(Mail Service)]
    Report --> Analytics[(Analytics DB)]
{{< /mermaid >}}


### Coupling to reduce unwanted dependencies

Coupling has a broader view in this context and comes as a way to quantify the dependency connections between modules, classes, functions, and smaller components of the system. We can understand the "coupled" concept **when a change in the code necessarily affects at least two components**, requiring a correction or adjustment in behavior.

**Having high coupling between modules is understood as a problem**, as it makes maintenance and testability so difficult - requiring retesting and revalidating a part of the system that shouldn't be affected - and also affects the modularity itself, reducing it and giving the illusion of having fewer modules due to dependencie between them.

#### Coupling Metrics

To determine an acceptable level of coupling, we can use techniques to identify useful metrics and help quantify it, such as:

**Afferent (Ca) and Efferent (Ce) Coupling**:

These are metrics that help measure the coupling of a module with other modules in the system and were popularized by the master Uncle Bob.

- Afferent (Ca): Measures the number of external components that depend on your component (incoming connections). Represents the responsibility of the module.
- Efferent (Ce): Measures the number of outgoing dependencies from your component to other external modules. Represents the instability of the module.

In this example, the `Billing Module` has **afferent coupling** because `Checkout` and `Orders` depend on it, while it has **efferent coupling** because it depends on `Payment Gateway` and `Shipping Service`.

{{< mermaid >}}
flowchart LR
    Checkout[Checkout Service] -- Ca --> Billing[Billing Module]
    Orders[Order Service] -- Ca --> Billing
    Billing -- Ce --> Payments[Payment Gateway]
    Billing -- Ce --> Shipping[Shipping Service]
{{< /mermaid >}}

**Consciousness**

It's a classification model of coupling forms introduced by Meilir Page-Jones (see more in the references) to extend the analysis of coupling and interdependencies to an object-oriented design. Consciousness can be **static**, when the dependency is identified in the code, or **dynamic**, when it depends on runtime behavior.

In action, we can use consciousness to identify how two components depend on each other and look for weaker forms of dependency. For example, sharing the name of a parameter between modules is safer than relying on the position of parameters, as a change in order can break the consumer.

{{< mermaid >}}
flowchart LR
    Client[Order Service] -->|amount, currency| Billing[Billing Module]
    Billing --> Contract[Payment Contract]
    Legacy[Legacy Client] -->|"values[0], values[1]"| Position[Positional Contract]
    Position -.-> Billing
{{< /mermaid >}}

> **Tip**: There are other ways of measurement besides various other types of coupling, but the important thing is to understand that **the weaker the coupling, the better**. And that cohesion and coupling go hand in hand, as a cohesive module tends to have fewer external dependencies and, therefore, lower coupling.

## Keeping the integrity of concepts with automated Guardrails

By now, we have seen how modularity, cohesion, and coupling assist in decision-making. Now, let's understand how we can use these concepts as software *guardrails* and how AI can help us automate software quality *checks*.

After implementing a module - or an initial version of the system - **we need to ensure that the modularity, cohesion, and coupling are being respected with every *Pull Request* opened**. Sonar or some other code analysis tool helps a lot to ensure code quality by avoiding CVEs, bugs, vulnerabilities, and performance issues, but it doesn't guarantee that the software architecture and design are being followed as specified in the project, as this is very particular to the context involving the creation of that system.

That's why we need automated mechanisms containing the rules of the architecture and design of that specific software. Next, I explain what **fitness functions** are and how we can use them as general rules that respect the architecture and design of the software.

## Fitness Functions to maintain the principles of software architecture and design

In general, **fitness functions** are defined as **any mechanism that provides an objective integrity assessment of some architectural characteristic or set of characteristics**. The term is borrowed from evolutionary computing, where a genetic algorithm uses a fitness function to measure how close a result is to achieving its goal.

These functions serve as **automated guardrails** in your continuous integration (CI/CD) pipeline. If a developer (or a code-generating AI) makes a change that violates an architectural decision, such as introducing a forbidden dependency or degrading performance, the fitness function will fail the build immediately, providing rapid feedback and preventing structural deterioration.

> **Tip**: These functions can be implemented in any programming language and at any step of the CI/CD pipeline. We can use ready-made tools like *ArchUnit (Java)*, *NetArchTest (C#)*, or even custom scripts in *Python*, *Bash*, etc.

The measurements of these functions are divided into three main categories:

1. **Structural Metrics**: Focus on internal quality and code design (e.g., cohesion, coupling, and modularity).
2. **Operational Metrics**: Measure the system in operation (e.g., resilience, latency, throughput).
3. **Process Metrics**: Evaluate the development flow (e.g., test coverage, deployment compliance).


### Practical Examples of Fitness Functions

Here are some common examples in pseudocode for each type of metric mentioned.

#### 1. Integrity between Code Layers (Structural Metric)

This test ensures that the classic layered structure (Presentation -> Business -> Persistence) is respected, preventing prohibited direct accesses (such as the interface layer calling the database directly).

```pseudocode
Procedure ValidateLayeredArchitectureCoupling()
    // 1. Map the project's packages/namespaces
    PresentationClasses = BuscarClassesNoPacote("com.sistema.apresentacao.*")
    BusinessClasses      = BuscarClassesNoPacote("com.sistema.negocio.*")
    PersistenceClasses = BuscarClassesNoPacote("com.sistema.persistencia.*")

    // 2. Rule: Presentation can only call Business
    For Each class In PresentationClasses Do
        If class.DependeDeAlguma(PersistenceClasses) Then
            FalharTeste("Architectural Violation: Presentation cannot access Persistence directly!")
        End If
    Next

    // 3. Rule: Persistence cannot call anyone above it
    For Each class In PersistenceClasses Do
        If class.DependeDeAlguma(BusinessClasses) Or class.DependeDeAlguma(PresentationClasses) Then
            FalharTeste("Architectural Violation: Persistence cannot depend on upper layers!")
        End If
    Next

    Retornar SUCCESS
End Procedure
```

#### 2. Software Resilience and Performance (Operational Metric)

Below, the function simulates a *stress test* window to ensure that the system maintains stability even under degraded network conditions.

```pseudocode
Procedure ValidateResilienceUnderLatency()
    // Instantiate the simulated load test executor
    LoadEnvironment = StartLoadEnvironment(ConcurrentUsers = 1000)

    // Inject artificial network latency (e.g., 300 ms)
    LoadEnvironment.InjectNetworkLatency(Milliseconds = 300)
    
    Results = LoadEnvironment.ExecuteTransactions(Quantity = 10000)
    
    // Asserções objetivas baseadas em métricas
    ErrorRate = Results.GetErrorMapping() / 10000
    MaxTime = Results.GetResponseTimePercentile99()

    Ensure(ErrorRate < 0.05, "Failure: Error rate under latency exceeded the 5% limit. Current: " + ErrorRate)
    Ensure(MaxTime < 10.0, "Failure: Response time (P99) exceeded 10 seconds under latency. Current: " + MaxTime)
    
    Retornar SUCCESS
End Procedure
```

#### 3. Operability (Minimum Production Standards)

In some architectures, no microservice or code is promoted if it is not "operable" by the DevOps/SRE teams. This process test ensures the presence of mandatory maintenance artifacts.

```pseudocode
Procedure ValidateReadinessForProduction()
    ProjectStructure = LoadProjectDirectory()
    
    // Guarantees minimum living documentation
    Ensure(ProjectStructure.FileExists("README.md"), "Operability: Missing README.md file for the service.")
    Ensure(ProjectStructure.FileExists("runbook.md"), "Operability: Missing runbook.md file containing incident mitigation guides.")
    
    // Guarantees that the microservice exposes an active *health check* endpoint for Kubernetes/orchestrator
    HealthController = ProjectStructure.FindClass("HealthCheckController")
    Ensure(HealthController != Null, "Operability: The service must expose an active '/health' endpoint.")
    
    Return SUCCESS
End Procedure
```

#### 4. Code Review with AI Agents

A practical use of AI is to include it as a step in the *Pull Request* review process.

Imagine that a change in the orders module starts importing the payments module directly, violating the rule that this communication should occur through the billing module. The agent can analyze the *diff*, consult the project's architectural rules, explain the violation, and suggest a more appropriate alternative.

In this flow, the AI acts as a reviewer capable of interpreting the change and providing context to the team. The result can be combined with a deterministic *fitness function*: if the rule is violated, the *pipeline* stops the *build* and returns the reason so that the change can be corrected.

{{< mermaid >}}
flowchart TD
    PR[Pull Request] --> Diff[Analyze diff]
    Rules[Architecture Rules] --> Agent[AI Review Agent]
    Diff --> Agent
    Agent --> Decision{Violation found?}
    Decision -->|No| Pass[Continue pipeline]
    Decision -->|Yes| Check[Run fitness function]
    Check --> Confirmed{Violation confirmed?}
    Confirmed -->|No| Pass
    Confirmed -->|Yes| Fail[Stop build]
    Fail --> Feedback[Send feedback to team]
{{< /mermaid >}}

### Fitness functions do not replace code analysis tools

Current tools like Qodana, SonarQube, ESLint, and others help maintain code quality but do not replace fitness functions that automatically check architectural compliance. Therefore, it is important to understand that **fitness functions are complementary to code analysis tools**, not substitutes. They act as an additional layer of protection, ensuring that architectural decisions are respected and that the software evolves sustainably. With so much code currently being generated by AI agents, **it is essential that these functions are implemented and maintained to prevent the degradation of the system's architecture over time.**

## Conclusion

Reviewing the fundamentals made me realize that their importance has increased drastically. Current code is cheap and generated quickly, so the developer/architect must focus even more on what surrounds the system to ensure that architecture and design do not deteriorate over time. This is a continuous job that requires discipline and attention to detail!

Modularity, cohesion, and coupling should not be treated merely as theoretical concepts. They can guide design decisions and also be transformed into fitness functions capable of continuously verifying the integrity of the architecture. When we combine this with *Harness Engineering* and the responsible use of AI, we can increase development speed without compromising quality.

In the end, AI can generate a lot of code, but it is still up to us to define the rules of the game. How have these guardrails been applied in your team? Share your experience in the comments.


## References and Recommended Readings

- [Fundamentals of Software Architecture: A Modern Engineering Approach](https://a.co/d/0gGgdFIW)
- [Cohesion and Coupling](https://www.geeksforgeeks.org/software-engineering/software-engineering-coupling-and-cohesion/)
- [Lesson 196 - Modularity and Architectural Styles](https://www.youtube.com/watch?v=Cmsyn7HK6YE)
- [Coupling.dev Modularity](https://coupling.dev/posts/core-concepts/modularity/)
- [Coupling.dev Afferent and Efferent Coupling](https://coupling.dev/posts/related-topics/afferent-and-efferent-coupling/)
- [Coupling.dev Connascence](https://coupling.dev/posts/related-topics/connascence/)
- [Monolithic vs Distributed Systems](http://geeksforgeeks.org/system-design/analysis-of-monolithic-and-distributed-systems-learn-system-design/)
- [Fitness Function Driven Development](https://www.thoughtworks.com/en-br/insights/articles/fitness-function-driven-development)
- [Fitness Functions in Architecture](https://www.infoq.com/articles/fitness-functions-architecture/)
- [Best Static Code Analysis Tools](https://blog.jetbrains.com/qodana/2026/04/best-static-code-analysis-tools/)
