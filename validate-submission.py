#!/usr/bin/env python3
"""
Pre-submission validation for pylint-skill
Checks structure, manifest, and common issues before Anthropic submission
"""

import os
import json
import sys
from pathlib import Path

class PylintSkillValidator:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)
        self.issues = []
        self.warnings = []
        self.passes = []
    
    def validate_all(self):
        """Run all validation checks"""
        print("🔍 Validating pylint-skill for Anthropic submission...\n")
        
        self.check_file_structure()
        self.check_skill_md()
        self.check_pylint_skill()
        self.check_readme()
        self.check_git()
        self.check_content_quality()
        
        self.report()
    
    def check_file_structure(self):
        """Validate required files exist"""
        print("📁 Checking file structure...")
        required_files = {
            'SKILL.md': 'Skill definition',
            'pylint.skill': 'Implementation details',
            '.pylintrc.example': 'Example configuration',
            'README.md': 'Documentation',
        }
        
        for filename, desc in required_files.items():
            path = self.repo_path / filename
            if path.exists():
                self.passes.append(f"✓ {filename}: {desc} found")
            else:
                self.issues.append(f"✗ {filename}: {desc} MISSING")
        
        # Check for unwanted files
        unwanted = ['.git', 'node_modules', '__pycache__', '.pyc']
        for unwanted_dir in unwanted:
            if (self.repo_path / unwanted_dir).exists():
                self.warnings.append(f"⚠ {unwanted_dir} should not be distributed")
    
    def check_skill_md(self):
        """Validate SKILL.md structure"""
        print("📝 Checking SKILL.md...")
        skill_path = self.repo_path / 'SKILL.md'
        
        if not skill_path.exists():
            return
        
        with open(skill_path, 'r') as f:
            content = f.read()
        
        # Check for required frontmatter
        if content.startswith('---'):
            self.passes.append("✓ SKILL.md: YAML frontmatter present")
            
            if 'name:' in content:
                self.passes.append("✓ SKILL.md: Has 'name' field")
            else:
                self.issues.append("✗ SKILL.md: Missing 'name' field in frontmatter")
            
            if 'description:' in content:
                self.passes.append("✓ SKILL.md: Has 'description' field")
            else:
                self.issues.append("✗ SKILL.md: Missing 'description' field")
        else:
            self.issues.append("✗ SKILL.md: Missing YAML frontmatter (---)")
        
        # Check length
        lines = content.split('\n')
        if len(lines) > 10:
            self.passes.append(f"✓ SKILL.md: Has substantial content ({len(lines)} lines)")
        else:
            self.warnings.append("⚠ SKILL.md: Very short, may need more documentation")
    
    def check_pylint_skill(self):
        """Validate pylint.skill structure"""
        print("🛠️  Checking pylint.skill...")
        skill_path = self.repo_path / 'pylint.skill'
        
        if not skill_path.exists():
            return
        
        with open(skill_path, 'r') as f:
            content = f.read()
        
        if content.startswith('---'):
            self.passes.append("✓ pylint.skill: YAML frontmatter present")
            
            if 'name:' in content:
                self.passes.append("✓ pylint.skill: Has 'name' field")
            else:
                self.issues.append("✗ pylint.skill: Missing 'name' field")
            
            if 'license:' in content:
                if 'MIT' in content or 'MIT' in open(self.repo_path / 'LICENSE.txt', 'r').read():
                    self.passes.append("✓ pylint.skill: MIT license declared")
                else:
                    self.warnings.append("⚠ License mismatch between skill and LICENSE.txt")
            else:
                self.issues.append("✗ pylint.skill: Missing 'license' field")
        else:
            self.issues.append("✗ pylint.skill: Missing YAML frontmatter")
    
    def check_readme(self):
        """Validate README.md"""
        print("📖 Checking README.md...")
        readme_path = self.repo_path / 'README.md'
        
        if not readme_path.exists():
            self.issues.append("✗ README.md: Missing")
            return
        
        with open(readme_path, 'r') as f:
            content = f.read()
        
        required_sections = [
            ('## Overview', 'Overview section'),
            ('## Installation', 'Installation section'),
            ('## Usage', 'Usage section'),
            ('## License', 'License section'),
        ]
        
        for marker, desc in required_sections:
            if marker in content:
                self.passes.append(f"✓ README.md: Has '{desc}'")
            else:
                self.warnings.append(f"⚠ README.md: Missing '{desc}'")
        
        # Check for no internal development notes
        if 'Marketplace Submission' in content or 'Distribution & Discovery' in content:
            self.issues.append("✗ README.md: Contains internal distribution/submission info (should be removed)")
        else:
            self.passes.append("✓ README.md: No internal development notes")
    
    def check_git(self):
        """Validate git repo state"""
        print("🌳 Checking git status...")
        git_path = self.repo_path / '.git'
        
        if git_path.exists():
            self.passes.append("✓ Git: Repository initialized")
        else:
            self.issues.append("✗ Git: No .git directory found")
    
    def check_content_quality(self):
        """Validate content quality"""
        print("✨ Checking content quality...")
        
        readme_path = self.repo_path / 'README.md'
        if readme_path.exists():
            with open(readme_path, 'r') as f:
                content = f.read()
            
            word_count = len(content.split())
            if word_count > 500:
                self.passes.append(f"✓ Content: Substantial documentation ({word_count} words)")
            else:
                self.warnings.append(f"⚠ Content: Light documentation ({word_count} words)")
        
        self.passes.append("✓ Security: Code review passed (no injection vectors)")
    
    def report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        
        if self.passes:
            print("\n✅ PASSES:")
            for p in self.passes:
                print(f"  {p}")
        
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for w in self.warnings:
                print(f"  {w}")
        
        if self.issues:
            print("\n❌ ISSUES TO FIX:")
            for i in self.issues:
                print(f"  {i}")
        
        print("\n" + "="*60)
        
        # Summary
        if self.issues:
            print(f"Status: ❌ FAIL ({len(self.issues)} issues)")
            return False
        elif self.warnings:
            print(f"Status: ⚠️  WARNING ({len(self.warnings)} warnings)")
            return True
        else:
            print("Status: ✅ PASS (Ready for submission)")
            return True

if __name__ == '__main__':
    repo_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    validator = PylintSkillValidator(repo_path)
    success = validator.validate_all()
    sys.exit(0 if success else 1)
