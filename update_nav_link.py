import glob
import os

target_str = '<li><a href="#">Vaginal Rejuvenation</a></li>'
target_str_adjusted = '<li><a href="../#">Vaginal Rejuvenation</a></li>'

new_str_root = '<li><a href="cosmetic-gynecology-treatmen/vaginal-rejuvenation-treatment.html">Vaginal Rejuvenation</a></li>'
new_str_sub = '<li><a href="vaginal-rejuvenation-treatment.html">Vaginal Rejuvenation</a></li>'

count = 0

# Process root HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_str in content:
        content = content.replace(target_str, new_str_root)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated root file: {file}')

# Process sub-directory HTML files
for file in glob.glob('cosmetic-gynecology-treatmen/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_str_adjusted in content:
        content = content.replace(target_str_adjusted, new_str_sub)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated sub file: {file}')

print(f'\nDone. Updated {count} file(s).')
