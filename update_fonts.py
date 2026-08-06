import glob

old_font = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
new_font = '<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sora:wght@400;500;600;700&display=swap" rel="stylesheet">'

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content_unix = content.replace('\r\n', '\n')
    if old_font in content_unix:
        content_unix = content_unix.replace(old_font, new_font)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content_unix)
        count += 1
        print(f'Updated: {file}')

print(f'\nDone. Updated {count} file(s).')
