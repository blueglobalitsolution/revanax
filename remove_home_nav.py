import glob

old_str = """                    <li><a href="index.html" class="active">HOME</a></li>"""
old_str2 = """                    <li><a href="index.html">HOME</a></li>"""

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    changed = False
    if old_str in content:
        content = content.replace(old_str, '')
        changed = True
    if old_str2 in content:
        content = content.replace(old_str2, '')
        changed = True
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated: {file}')

print(f'\nDone. Updated {count} file(s).')
