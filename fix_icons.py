import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_func = '''def get_icon_for_calculator(slug: str) -> str:
    icons = {
        "compound-interest": "\U0001F4C8",
        "debt-payoff": "\U0001F4B3",
        "emergency-fund": "\U0001F6E1\uFE0F",
        "savings-rate": "\U0001F3E6",
        "loan-amortization": "\U0001F3E0",
        "salary-to-hourly": "\u23F1\uFE0F",
        "goal-planner": "\U0001F3AF",
        "expense-ratio": "\U0001F4C9",
        "apr-apy": "\U0001F504",
        "dollar-cost-averaging": "\U0001F4C5",
        "idx-stock-screener": "\U0001F4CA",
        "screener-saham-idx": "\U0001F4CA",
    }
    return icons.get(slug.replace(".html", ""), "\U0001F527")'''

content = re.sub(r'def get_icon_for_calculator\(slug: str\) -> str:.*?return icons\.get\(slug\.replace\("\.html", ""\), ".*?"\)', new_func, content, flags=re.DOTALL)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)
