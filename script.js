document.addEventListener('DOMContentLoaded', () => {
    console.log('ReevanaX Site Loaded');
    
    // Add simple active state logic for navigation
    const navLinks = document.querySelectorAll('.nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            if (link.getAttribute('href') === '#') {
                e.preventDefault();
                navLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            }
        });
    });
});
