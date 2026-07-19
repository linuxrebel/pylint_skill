---
name: pylint
description: Run pylint on Python files to lint code for style, errors, and best practices. Trigger with "lint this", "run pylint on", "check code quality", or when analyzing Python files for violations.
argument-hint: "<Python file path or directory>"
---

# /pylint

Lint Python code for style violations, errors, and code quality issues using pylint.

## Usage

```
/pylint <Python file or directory path>
```

Analyze the provided Python file(s) with pylint: @$1

If no specific file or path is provided, ask what to lint.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                      PYLINT ANALYSIS                               │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                       │
│  ✓ Single file or directory scanning                             │
│  ✓ Style issues (PEP 8 compliance)                               │
│  ✓ Error detection (undefined variables, imports)                │
│  ✓ Best practices (unused variables, missing docstrings)         │
│  ✓ Complexity analysis (cyclomatic complexity, lines of code)    │
│  ✓ Structured report with severity levels                        │
│  ✓ Score calculation (0.0-10.0)                                  │
├─────────────────────────────────────────────────────────────────┤
│  CUSTOMIZABLE                                                     │
│  + Custom pylint config (.pylintrc)                              │
│  + Disable/enable specific message categories                    │
│  + Set minimum confidence thresholds                             │
│  + Configure max line length and complexity limits               │
└─────────────────────────────────────────────────────────────────┘
```

## Message Categories

### Error (E)
- Undefined variables
- Import errors
- Syntax errors
- Invalid function calls

### Warning (W)
- Unused imports
- Unused variables
- Unreachable code
- Missing return statements

### Convention (C)
- PEP 8 naming violations
- Missing docstrings
- Whitespace issues
- Line length

### Refactor (R)
- Too many branches/arguments
- Duplicate code
- Complex functions
- Too many attributes

### Informational (I)
- Suppressed messages
- Locally disabled checks
- File ignores

## Output Format

```markdown
## Pylint Analysis: [filename/directory]

### Summary
- **Score**: 8.5/10
- **Messages**: 15 (3 errors, 4 warnings, 8 conventions)
- **Files Analyzed**: 5

### Critical Issues
| File | Line | Message | Type |
|------|------|---------|------|
| app.py | 42 | Undefined variable 'config' | E |
| utils.py | 15 | Unused import 'os' | W |

### Style Issues
| File | Line | Message | Type |
|------|------|---------|------|
| main.py | 5 | Missing module docstring | C |
| handler.py | 120 | Line too long (105 > 100) | C |

### Refactoring Suggestions
| File | Line | Message | Type |
|------|------|---------|------|
| core.py | 50 | Function too complex (12 branches) | R |

### Passing Files
- clean_module.py ✓

## Tips

1. **Single file**: `/pylint path/to/file.py`
2. **Directory**: `/pylint path/to/package/`
3. **Disable checks**: Modify or create `.pylintrc` in project root
4. **Focus area**: "Focus on errors only" to ignore style issues
5. **Specific message**: "Show only E-type messages" filters output
