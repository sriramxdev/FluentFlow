"""Synthesize and self-heal a Mermaid diagram with Gemini."""
from __future__ import annotations
import json, os, subprocess, sys, urllib.request
from pathlib import Path
OUTPUT = Path(os.getenv("DIAGRAM_OUTPUT", "generated/diagram.mmd"))
def ask_gemini(prompt: str) -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key: raise RuntimeError("GEMINI_API_KEY is required for pipeline synthesis.")
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    request = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent", data=body, headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(request, timeout=60) as response: return json.load(response)["candidates"][0]["content"]["parts"][0]["text"]
def extract_mermaid(text: str) -> str:
    if "```" not in text: return text.strip()
    chunks = text.split("```")
    for chunk in chunks:
        if chunk.strip().lower().startswith("mermaid"): return chunk.strip()[7:].strip()
    return chunks[1].strip()
def validate(path: Path) -> tuple[bool, str]:
    result = subprocess.run(["node", "scripts/validate_mermaid.mjs", str(path)], text=True, capture_output=True)
    return result.returncode == 0, (result.stdout + result.stderr).strip()
def main() -> int:
    specification = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    prompt = "Return only valid Mermaid flowchart code. No markdown fences. Translate this specification into a clear architecture diagram:\n" + specification
    feedback = ""; OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(1, 4):
        OUTPUT.write_text(extract_mermaid(ask_gemini(prompt + feedback)) + "\n", encoding="utf-8")
        valid, trace = validate(OUTPUT)
        if valid: print(f"Synthesis validated on attempt {attempt}: {OUTPUT}"); return 0
        feedback = f"\nThe compiler failed with this trace. Return corrected Mermaid only:\n{trace}\n"
    print("Gemini could not produce a compilable diagram after three attempts.", file=sys.stderr); return 1
if __name__ == "__main__": raise SystemExit(main())
