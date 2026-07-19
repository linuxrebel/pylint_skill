# pylint-skill

A Claude skill for linting Python code with pylint, providing structured analysis of style violations, errors, and code quality issues.

## Overview

This skill integrates pylint into Claude workflows, enabling:

- **Single file or directory scanning** — Analyze one `.py` file or an entire package
- **Style compliance** — PEP 8 and naming convention checks
- **Error detection** — Undefined variables, import errors, syntax issues
- **Best practices** — Unused imports/variables, missing docstrings, complexity analysis
- **Structured reporting** — JSON-based parsing with severity levels (Error, Warning, Convention, Refactor)
- **Score calculation** — 0.0-10.0 rating for overall code quality

## Installation

### 1. Clone the Repo

```bash
git clone https://github.com/linuxrebel/pylint-skill.git
cd pylint-skill
```

### 2. Install pylint

Choose one of the following installation methods:

**User-level pip install:**
```bash
pip install pylint --user
```

**System-wide pip install:**
```bash
pip install pylint
# or with sudo if needed
sudo pip install pylint
```

**Package manager (distro-specific):**

Fedora/RHEL/CentOS:
```bash
sudo dnf install python3-pylint
```

Debian/Ubuntu:
```bash
sudo apt install pylint
```

Arch:
```bash
sudo pacman -S pylint
```

Alpine:
```bash
apk add pylint
```

macOS (Homebrew):
```bash
brew install pylint
```

### 3. Add to Claude Desktop

Copy only the necessary skill files to your Claude Desktop skills directory:

**macOS/Linux:**
```bash
mkdir -p ~/.config/claude/skills/pylint-skill
cp SKILL.md pylint.skill pylintrc ~/.config/claude/skills/pylint-skill/
cd ~/.config/claude/skills/pylint-skill/
mv pylintrc .pylintrc
```

**Windows:**
```powershell
$skillDir = "$env:APPDATA\Claude\skills\pylint-skill"
New-Item -ItemType Directory -Force -Path $skillDir
Copy-Item SKILL.md, pylint.skill, pylintrc $skillDir
cd $skillDir
Rename-Item pylintrc .pylintrc
```

Then restart Claude Desktop.

**Files needed in skills directory:**
- `SKILL.md` — Skill definition and documentation
- `pylint.skill` — Implementation details
- `.pylintrc` — Pylint configuration (created by renaming `pylintrc` from repo)

**Note:** The repository contains `pylintrc` (without the dot prefix) for visibility in version control. When installing, rename it to `.pylintrc` (with the dot) to make it a hidden configuration file. Do NOT copy `.git/`, `README.md`, or other files to keep the installation clean.

### 4. Add to Claude Code / Cowork

If using Claude Code (VS Code, JetBrains, Terminal) or Cowork, copy the necessary skill files to your local skills directory:

**VS Code / JetBrains / Terminal:**
```bash
# Skills are typically stored in:
# ~/.config/claude/skills/ (Linux)
# ~/Library/Application\ Support/Claude/skills/ (macOS)
# %APPDATA%\Claude\skills\ (Windows)

mkdir -p ~/.config/claude/skills/pylint-skill
cp SKILL.md pylint.skill pylintrc ~/.config/claude/skills/pylint-skill/
cd ~/.config/claude/skills/pylint-skill/
mv pylintrc .pylintrc
```

Or set via environment variable:
```bash
export CLAUDE_SKILLS_DIR="/path/to/skills"
mkdir -p $CLAUDE_SKILLS_DIR/pylint-skill
cp SKILL.md pylint.skill pylintrc $CLAUDE_SKILLS_DIR/pylint-skill/
cd $CLAUDE_SKILLS_DIR/pylint-skill/
mv pylintrc .pylintrc
```

Then restart Claude Code or your IDE extension.

### 5. Add to iOS/Android (Claude Desktop App)

On mobile devices, Claude Desktop stores skills in the app's local storage. Use the Claude app's file management:

**iOS:**
1. Open the Claude app
2. Go to Settings → Skills
3. Tap "Add Skill" or "Import Skill"
4. Copy the contents of `SKILL.md` and `pylint.skill` into the respective fields
5. Add `.pylintrc.example` as a reference file if the app supports it

**Android:**
1. Open the Claude app
2. Navigate to Settings → Skills
3. Tap the "+" button to add a new skill
4. Paste the contents of `SKILL.md` and `pylint.skill`
5. Save the skill configuration

Alternatively, if using iCloud Drive (iOS) or Google Drive (Android) integration:
1. Upload `SKILL.md`, `pylint.skill`, and `.pylintrc.example` to your cloud storage
2. Open Claude app and link to your cloud drive
3. Import the skill files from there

## Platform Support

- ✅ **Claude Desktop** (macOS, Linux, Windows, iOS, Android)
- ✅ **Claude Code** (VS Code, JetBrains, Terminal)
- ✅ **Cowork** (CLI)

All platforms support local skills installation.

## Usage

### Basic Linting

```
/pylint /path/to/file.py
```

Analyze a single Python file and receive a structured report.

### Directory Analysis

```
/pylint /path/to/package/
```

Lint all Python files in a directory recursively.

### With Custom Config

If a `.pylintrc` exists in your project root, it's used automatically:

```bash
pylint --output-format=json --exit-zero --rcfile=.pylintrc <path>
```

### Filter by Type

Tell Claude to focus on specific message types:

- "Show only errors" → Ignores style/refactor suggestions
- "Focus on complexity" → Highlights cyclomatic complexity issues
- "Convention issues only" → PEP 8 and naming violations

## Output

Reports include:

- **Summary** — Overall score, message counts, files analyzed
- **Critical Issues** — Errors (undefined vars, import errors, syntax)
- **Warnings** — Unreachable code, missing returns, unused imports
- **Style Issues** — PEP 8 violations, docstrings, line length
- **Refactor Suggestions** — Complex functions, duplicate code, too many args
- **Passing Files** — Successfully linted files with no issues

Example output:

```markdown
## Pylint Analysis: myapp/

### Summary
- **Score**: 8.5/10
- **Messages**: 15 (3 errors, 4 warnings, 8 conventions)
- **Files Analyzed**: 5

### Critical Issues
| File | Line | Message | Type |
|------|------|---------|------|
| handlers.py | 42 | Undefined variable 'config' | E |
| utils.py | 15 | Unused import 'os' | W |
```

## Skill Files

- **SKILL.md** — User-facing documentation and trigger descriptions
- **pylint.skill** — Implementation details (execution steps, parsing, report formatting)
- **LICENSE.txt** — GPL-3.0 license

## How It Works

1. **Validation** — Check that the path exists and contains Python files
2. **Installation check** — Ensure pylint is available
3. **Execution** — Run pylint with JSON output: `pylint --output-format=json --exit-zero <path>`
4. **Parsing** — Extract errors, warnings, conventions, refactor suggestions from JSON
5. **Formatting** — Organize findings by severity and file, calculate score

## Message Categories

| Type | Examples |
|------|----------|
| **Error (E)** | Undefined variables, import errors, syntax errors |
| **Warning (W)** | Unused imports, unreachable code, missing returns |
| **Convention (C)** | PEP 8 naming, missing docstrings, line length |
| **Refactor (R)** | Too complex, too many args, duplicate code |
| **Informational (I)** | Suppressed messages, local disables |

## Customization

### Project-Level Config (`.pylintrc`)

Create a `.pylintrc` file in your project root to customize pylint behavior. The skill automatically detects and uses it.

**Example: Enforce camelCase and 4-space indentation**

```ini
[FORMAT]
indent-string='    '  # 4 spaces instead of 2

[NAMING]
variable-naming-style=camelCase
argument-naming-style=camelCase
function-naming-style=camelCase

[DESIGN]
max-line-length=100
max-locals=15
max-branches=12
```

See [`.pylintrc.example`](.pylintrc.example) in this repo for more options.

### Company/Team Standards

For firm-wide standards:

1. **Version control your `.pylintrc`** in your project or organization repo
2. **Document overrides** — Link to your config in team docs
3. **Use pylint plugins** — Install custom rule packages:
   ```bash
   pip install pylint-django pylint-flask  # etc.
   ```
   Then reference in `.pylintrc`:
   ```ini
   [MASTER]
   load-plugins=pylint_django,pylint_flask
   ```

### Extending the Skill

Fork this repo to create a company-specific variant:

```bash
git clone https://github.com/linuxrebel/pylint-skill.git pylint-skill-acme
cd pylint-skill-acme
# Add your .pylintrc with company standards
git add .pylintrc
git commit -m "feat: add ACME Corp pylint standards"
```

Then distribute to your team as a custom skill.

## Customizing for Your Team/Project

### Default Behavior

By default, the skill uses the `.pylintrc` file distributed with the installation (renamed from `pylintrc` in the repo).

### Extending with Your Own .pylintrc

If you need custom pylint rules for your team or organization:

1. **Copy the default configuration** as a starting point:
   ```bash
   cp ~/.config/claude/skills/pylint-skill/.pylintrc my-project/.pylintrc
   ```

2. **Customize your `.pylintrc`** with your team's standards:
   ```ini
   [FORMAT]
   indent-string='    '  # 4 spaces
   
   [NAMING]
   variable-naming-style=camelCase
   ```

3. **Update the skill to use your config** (optional):
   - Edit `pylint.skill` in your skills directory
   - Find the line: `pylint --output-format=json --exit-zero <path>`
   - Change to: `pylint --rcfile=/path/to/your/.pylintrc --output-format=json --exit-zero <path>`
   
   **Note:** Only modify the skill if you need to enforce a specific `.pylintrc` globally. Most users can simply commit `.pylintrc` to their project root, and pylint will find it automatically.

## Tips

1. **Disable noisy checks** — Suppress `missing-docstring` for codebases without docs
2. **Use plugins for domain rules** — Install `pylint-django`, `pylint-flask`, etc. for framework-specific checks
3. **CI integration** — Use pylint output in CI/CD pipelines to enforce standards
4. **Combined review** — Pair with `/code-review` skill for human judgment + automated checks
5. **Fork for company standards** — Create a company-specific variant with your `.pylintrc` baked in

## Related Skills

- `/code-review` — Manual code review for security, performance, correctness
- `/debug` — Fix specific errors and issues
- `/test` — Verify code correctness with unit tests

## License

MIT — See LICENSE.txt

## Author

James Sparenberg (@linuxrebel)
