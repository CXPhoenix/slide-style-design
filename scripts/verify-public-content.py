#!/usr/bin/env python3
"""Check publication candidates for known private artifacts; never print values.

Checks tracked files plus non-ignored new files in the working tree. This is a
bounded guard, not a complete secret scanner or a Git-history erasure check.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'private conversation address': re.compile(r'(?:https?://)?chatgpt\.com/(?:c/|g/[^\s<>]*?/c/)[A-Za-z0-9-]+'),
    'full browser sidebar': re.compile(r'app-shell-sidebar'),
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'credential token': re.compile(r'\b(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-proj-[A-Za-z0-9_-]{30,})\b'),
    'embedded capture': re.compile(r'data:image/(?:png|jpeg);base64,'),
}
HOME = re.compile(r'/Users/[A-Za-z0-9_.-]+/')

def main():
    names = set()
    for args in (['ls-files', '-z'], ['ls-files', '--others', '--exclude-standard', '-z']):
        names.update(subprocess.check_output(['git', *args], cwd=ROOT).decode().split('\0'))
    findings = []
    checked = 0
    for name in sorted(names - {''}):
        path = ROOT / name
        if not path.is_file():
            continue
        checked += 1
        if name.startswith('.proj.tickets/') and path.suffix.lower() in {'.png', '.jpg', '.jpeg'}:
            findings.append((name, 'raw browser evidence image'))
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for category, pattern in PATTERNS.items():
            if name == 'scripts/verify-public-content.py' and category == 'full browser sidebar':
                continue  # The guard names the marker it detects.
            if category == 'embedded capture' and name.startswith(('.agents/', '.claude/')):
                continue  # Public export-test fixtures, not browser evidence.
            if pattern.search(text):
                findings.append((name, category))
        # Vendor skills contain public examples/regex, confirmed separately.
        if not name.startswith(('.agents/', '.claude/')) and HOME.search(text):
            findings.append((name, 'personal home path'))
    for name, category in findings:
        print(f'FAIL {category}: {name}')
    print(f'{"FAIL" if findings else "PASS"}: {checked} working-tree publication files; {len(findings)} known-pattern findings')
    print('Git history, unknown credential formats and remote copies require separate review.')
    return bool(findings)

if __name__ == '__main__':
    sys.exit(main())
