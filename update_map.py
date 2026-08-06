import glob

old_map = '<img src="https://via.placeholder.com/600x300?text=Map+Placeholder" alt="Map Location" style="width: 100%; border-radius: 8px; border: 1px solid #ddd;">'
new_map = '<iframe src="https://maps.google.com/maps?q=ReevanaX%20%E2%80%93%20Skin,%20Hair,%20Laser,%20Plastic%20Surgery%20%26%20Aesthetic%20Clinic,%20Surat&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="300" style="border:0; border-radius: 8px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_map in content:
        content = content.replace(old_map, new_map)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated map in: {file}')

print(f'\nDone. Updated {count} file(s).')
