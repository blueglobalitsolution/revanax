import glob

old_fa = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
new_fa = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">'

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    
    if old_fa in content:
        content = content.replace(old_fa, new_fa)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Updated FontAwesome link in {count} file(s).')
