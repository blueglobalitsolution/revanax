import os
import glob
import re

# Pages to create with their exact menu text
pages_data = [
    ("Vaginal Tightening with Advance Technology", "vaginal-tightening-with-advance-technology.html"),
    ("Vaginal PRP", "vaginal-prp.html"),
    ("Chronic Vaginal Infection Laser Treatment", "chronic-vaginal-infection-laser-treatment.html"),
    ("O-Shot & G-Shot for Enhacing Sexual Pleasure", "o-shot-g-shot-for-enhacing-sexual-pleasure.html"),
    ("Laser Vaginoplasty", "laser-vaginoplasty.html"),
    ("Surgical Vaginoplasty", "surgical-vaginoplasty.html"),
    ("Vaginal Septum Removal", "vaginal-septum-removal.html"),
    ("Labiaplasty", "labiaplasty.html"),
    ("Clitoral Hood Plasty", "clitoral-hood-plasty.html"),
    ("Hymenoplasty", "hymenoplasty.html")
]

folder = 'cosmetic-gynecology-treatmen'
template_file = os.path.join(folder, 'vaginal-rejuvenation-treatment.html')

with open(template_file, 'r', encoding='utf-8') as f:
    template_html = f.read()

# 1. Create the new pages based on the template
for title, filename in pages_data:
    filepath = os.path.join(folder, filename)
    # Replace the badge text
    new_html = re.sub(r'>Vaginal Rejuvenation</span>', f'>{title}</span>', template_html)
    # Replace the H1
    new_html = re.sub(r'<h1>.*?</h1>', f'<h1 style="text-align: center; color: var(--secondary-color); font-family: \'Sora\', sans-serif; font-size: 28px; margin-bottom: 50px;">{title} Treatment at ReevanaX, Surat</h1>', new_html)
    # Replace the h1 that I actually used in the template (I didn't use <h1> tags for it, wait, I used <h1 style="...">)
    new_html = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 style="text-align: center; color: var(--secondary-color); font-family: \'Sora\', sans-serif; font-size: 28px; margin-bottom: 50px;">{title} Treatment at ReevanaX, Surat</h1>', new_html)
    # Replace <title>
    new_html = re.sub(r'<title>.*?</title>', f'<title>{title} - ReevanaX</title>', new_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created: {filepath}")

# 2. Update navigation menus across all root HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    for title, filename in pages_data:
        old_link = f'<li><a href="#">{title}</a></li>'
        new_link = f'<li><a href="{folder}/{filename}">{title}</a></li>'
        if old_link in content:
            content = content.replace(old_link, new_link)
            changed = True
            
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in root: {file}")

# 3. Update navigation menus across all sub-folder HTML files
for file in glob.glob(f'{folder}/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    for title, filename in pages_data:
        # Check both adjusted and non-adjusted links
        old_link1 = f'<li><a href="../#">{title}</a></li>'
        old_link2 = f'<li><a href="#">{title}</a></li>'
        new_link = f'<li><a href="{filename}">{title}</a></li>'
        
        if old_link1 in content:
            content = content.replace(old_link1, new_link)
            changed = True
        if old_link2 in content:
            content = content.replace(old_link2, new_link)
            changed = True
            
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in sub: {file}")

print("Done generating pages and updating links.")
