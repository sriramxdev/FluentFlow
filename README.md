# FluentFlow 🌊

> **GitOps-Driven Architecture & Diagram-as-Code Synthesizer with Self-Healing CI/CD Validation**

[![Pages Deployment](https://github.com/sriramxdev/FluentFlow/actions/workflows/deploy.yml/badge.svg)](https://github.com/sriramxdev/FluentFlow/actions)
[![Diagram Pipeline](https://github.com/sriramxdev/FluentFlow/actions/workflows/diagram_pipeline.yml/badge.svg)](https://github.com/sriramxdev/FluentFlow/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

FluentFlow is an automated, GitOps-aligned Diagram-as-Code (DaC) synthesis platform. It translates unstructured technical specifications, protocol definitions, and service interactions into verified, production-grade Mermaid.js architecture diagrams.

Traditional LLM diagram generators produce raw text outputs that frequently fail to render due to syntax hallucinations, unsupported characters, or malformed Abstract Syntax Trees (ASTs). FluentFlow eliminates broken outputs through an automated **Closed-Loop Self-Healing CI/CD Pipeline**: generated code is compiled and validated inside headless GitHub Actions runners, catching compiler exceptions and re-prompting the model with compiler stack traces until strict validation passes.

---

## 🏛️ System Architecture

FluentFlow operates as a decoupled system combining an edge-rendered static client, an event-driven continuous integration runner, and a multi-stage validation engine:

```mermaid
graph TD
    subgraph "1. Client Layer (Astro + Tailwind)"
        A[User Input / Spec Payload] --> B[FileUpload Component]
        B -->|Client Validation| C{MIME Whitelist}
        C -->|Valid: JSON / PDF / TXT / MD / YAML| D[State Orchestrator]
        C -->|Rejected: Binary Images| E[Error Banner]
        D -->|Custom Event Dispatch| F[DiagramCanvas Component]
    end

    subgraph "2. GitOps CI/CD Self-Healing Engine (GitHub Actions)"
        D -.->|Repository Dispatch Event| G[diagram_pipeline.yml Runner]
        G --> H[Environment Setup: Pixi]
        H --> I[scripts/synthesize.py]
        I --> J[Gemini API: Structured Prompt]
        J --> K[Raw Mermaid Output]
        K --> L[scripts/validate_mermaid.mjs]
        L -->|Syntax Check via @mermaid-js/mermaid-cli| M{AST Valid?}
        M -->|Compile Error / Non-Zero Exit| N[Feedback Generator]
        N -->|Append Error Trace to Context| J
        M -->|Exit Code 0: Success| O[Verified Artifact Export]
    end

    subgraph "3. Artifact Delivery & Presentation"
        O -.->|Generated Artifact| F
        F -->|Client Fallback Engine| P[Interactive Pan / Zoom Canvas]
        P --> Q[Vector Export: SVG]
        P --> R[Raster Export: PNG]
        P --> S[Document Export: PDF]
    end