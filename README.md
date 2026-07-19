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

1. Open Claude Desktop Settings → Skills
2. Click the "Add" button and select "Upload a skill"
3. Upload this repository as a `.zip` file (or just upload `SKILL.md`)
4. Claude Desktop will install the skill automatically and it's available immediately—no restart needed

**Files to upload:**
- `SKILL.md` — Skill definition (required)
- `pylint.skill` — Implementation details (recommended)

Or upload as a `.zip` containing both files.

### 4. Add to Claude Code / Cowork

Copy the skill files to your local skills directory:

**macOS/Linux:**
```bash
mkdir -p .claude/skills/pylint
cp SKILL.md pylint.skill .claude/skills/pylint/
```

**Windows:**
```powershell
$skillDir = "$env:USERPROFILE\.claude\skills\pylint"
New-Item -ItemType Directory -Force -Path $skillDir
Copy-Item SKILL.md, pylint.skill $skillDir
```

Then start a new Claude Code session. The skill will be available automatically on the next run.

**Files needed:**
- `SKILL.md` — Skill definition and documentation
- `pylint.skill` — Implementation details

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

## License

MIT — See LICENSE.txt

## Author

James Sparenberg (@linuxrebel)
