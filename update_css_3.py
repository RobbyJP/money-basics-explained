import re

with open('templates/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the calculator container look more integrated
css = re.sub(r'\.calculator-container\s*{[^}]+}', '''.calculator-container {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 32px;
  margin: 32px 0 48px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}''', css)

# Style headings to look less editorial
css = re.sub(r'h1\s*{[^}]+}', '''h1 {
  font-size: 2.2rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-top: 0;
  margin-bottom: 16px;
  line-height: 1.2;
}''', css)

with open('templates/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css for tool pages")
