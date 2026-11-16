#!/usr/bin/env python3
"""Check relative Markdown file links and public-safe fixture email syntax."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)]+)\)')
EMAIL_RE = re.compile(r'\b[A-Za-z0-9._%+\-]+@(?:[A-Za-z0-9\-]+\.)+[A-Za-z]{2,}\b')

def check(root=ROOT):
    errors=[]
    for file in sorted(root.rglob('*.md')):
        content=file.read_text(encoding='utf-8')
        for match in LINK_RE.finditer(content):
            target=match.group(1).strip().split(' ')[0].strip('<>')
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            rel=target.split('#', 1)[0]
            if rel and not (file.parent / rel).exists():
                errors.append(f'{file.relative_to(root)}: broken link {target}')
        for email in EMAIL_RE.findall(content):
            if not email.endswith(('.invalid','.example','.test')):
                errors.append(f'{file.relative_to(root)}: review non-example email {email}')
    for file in sorted((root/'labs'/'data').glob('*.csv')):
        for email in EMAIL_RE.findall(file.read_text(encoding='utf-8')):
            if not email.endswith(('.invalid','.example','.test')):
                errors.append(f'{file.relative_to(root)}: review non-example email {email}')
    return errors

def main():
    errors=check()
    if errors:
        print('\n'.join(errors));sys.exit(1)
    print('PASS: relative Markdown links exist; example email checks clear.')

if __name__=='__main__':
    main()
