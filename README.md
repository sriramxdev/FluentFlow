# FluentFlow

FluentFlow is a free-tier Diagram-as-Code synthesis engine. It turns technical specifications into Mermaid architecture diagrams, validates generated source, and retries Gemini synthesis when the Mermaid compiler reports a failure.

## Stack

- Astro 5 with Tailwind CSS, hosted on GitHub Pages
- GitHub Actions for static deployment and diagram pipeline execution
- Google AI Studio Gemini `gemini-2.5-flash` via `GEMINI_API_KEY`
- Mermaid for rendering and `@mermaid-js/mermaid-cli` for CI validation
- Pixi for Python 3.11 and Node.js task orchestration

## Local development

```bash
pixi install
pixi run npm install
pixi run dev
```

The UI has an offline Mermaid fallback, so presets and local text input work without credentials. For synthesis:

```bash
GEMINI_API_KEY=your-key pixi run synthesize path/to/spec.txt
```

Add `GEMINI_API_KEY` as a repository Actions secret. All application copy, navigation, presets, supported file rules, and Mermaid theme variables are data-driven under `src/data/`.
