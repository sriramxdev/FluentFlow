import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { existsSync } from 'node:fs';
const execFileAsync = promisify(execFile);
const input = process.argv[2] ?? 'diagram.mmd';
if (!existsSync(input)) { console.error(`Mermaid source not found: ${input}`); process.exit(2); }
try { await execFileAsync('npx', ['--yes', 'mmdc', '-i', input, '-o', '/tmp/fluentflow-validation.svg', '-b', 'transparent'], { maxBuffer: 1024 * 1024 }); console.log(`Validated Mermaid source: ${input}`); } catch (error) { console.error(error?.stderr || error?.message || error); process.exit(1); }
