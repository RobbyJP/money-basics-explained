import re

with open('templates/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make body full width, remove side paddings from body to give it to containers
css = re.sub(r'body\s*{[^}]+}', '''body {
  font-family: var(--font-sans);
  margin: 0;
  padding: 0;
  line-height: 1.65;
  color: var(--ink);
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  max-width: 1100px;
  margin: 0 auto;
  padding: 32px 16px 64px;
  width: 100%;
  flex: 1;
}
''', css)

# Fix site header to be full width
css = re.sub(r'\.site-header\s*{[^}]+}', '''.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  height: 70px;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
  width: 100%;
}''', css)

# Make site title look like a logo
css = re.sub(r'\.site-title\s*{[^}]+}', '''.site-title {
  font-size: 1.25rem;
  font-weight: 800;
  text-decoration: none;
  color: var(--ink);
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  gap: 8px;
}''', css)

# Adjust footer
css = re.sub(r'\.site-footer\s*{[^}]+}', '''.site-footer {
  text-align: center;
  padding: 40px 16px;
  margin-top: auto;
  border-top: 1px solid var(--line);
  background: var(--surface);
  width: 100%;
}''', css)

# Add an emoji to the site title using CSS pseudo-element
css += '''
.site-title::before {
  content: "🔧";
  font-size: 1.4rem;
}
'''

with open('templates/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css extensively")
