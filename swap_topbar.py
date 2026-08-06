import glob

old_str = """            <div class="top-bar-left">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-pinterest-p"></i></a>
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
                <a href="#"><i class="fa-brands fa-threads"></i></a>
            </div>
            <div class="top-bar-right">
                <span><i class="fab fa-whatsapp"></i> +91 88662 20272</span>
                <span><i class="fas fa-phone-alt"></i> +91 88662 20273</span>
                <span><i class="fas fa-phone-alt"></i> +91 88662 20274</span>
                <span><i class="fas fa-envelope"></i> info.reevanax@gmail.com</span>
            </div>"""

new_str = """            <div class="top-bar-left">
                <span><i class="fab fa-whatsapp"></i> +91 88662 20272</span>
                <span><i class="fas fa-phone-alt"></i> +91 88662 20273</span>
                <span><i class="fas fa-phone-alt"></i> +91 88662 20274</span>
                <span><i class="fas fa-envelope"></i> info.reevanax@gmail.com</span>
            </div>
            <div class="top-bar-right">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-pinterest-p"></i></a>
                <a href="#"><i class="fab fa-linkedin-in"></i></a>
                <a href="#"><i class="fa-brands fa-threads"></i></a>
            </div>"""

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated: {file}')

print(f'\nDone. Updated {count} file(s).')
