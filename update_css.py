import re

with open('templates/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make it wider
css = re.sub(r'max-width:\s*860px;', 'max-width: 1100px;', css)

# Make the header look like a web app header
# Currently it's: .site-header { display: flex; align-items: center; justify-content: space-between; padding: 24px 0; border-bottom: 1px solid var(--line); margin-bottom: 32px; }
css = re.sub(r'\.site-header\s*{[^}]+}', '.site-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; border-bottom: 1px solid var(--line); margin: 0 -16px 32px; background: var(--surface); box-shadow: 0 1px 3px rgba(0,0,0,0.05); border-radius: 0 0 12px 12px; }', css)

# Update hero section
css = re.sub(r'\.hero\s*{[^}]+}', '.hero { text-align: center; padding: 40px 20px; background: var(--surface); border: 1px solid var(--line); border-radius: 16px; margin-bottom: 32px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }', css)

# Change background color to feel more "app-like"
css = re.sub(r'--bg:\s*#f4f6fb;', '--bg: #f9fafb;', css)

with open('templates/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
