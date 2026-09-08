import os
import re

updates = {
    "compound-interest-calculator-with-monthly-contributions.md": {
        "title": "Compound Interest Calculator",
        "description": "Calculate compound growth over time with optional monthly contributions."
    },
    "debt-snowball-vs-debt-avalanche.md": {
        "title": "Debt Payoff Calculator",
        "description": "Compare the Debt Snowball vs Avalanche methods to find the fastest way out of debt."
    },
    "emergency-fund-how-much-is-enough.md": {
        "title": "Emergency Fund Calculator",
        "description": "Estimate exactly how much you need in your emergency fund based on your living expenses."
    },
    "how-to-calculate-savings-rate.md": {
        "title": "Savings Rate Calculator",
        "description": "Calculate your true savings rate and see when you'll reach financial independence."
    },
    "id-screener-saham-idx.md": {
        "title": "Screener Saham BEI",
        "description": "Saring saham Bursa Efek Indonesia berdasarkan valuasi, profitabilitas, dan pertumbuhan."
    },
    "idx-stock-screener.md": {
        "title": "IDX Stock Screener",
        "description": "Screen Indonesian (IDX) stocks by valuation, ROE, growth, and dividend yield."
    },
    "loan-amortization-explained.md": {
        "title": "Loan Amortization Calculator",
        "description": "Generate a complete amortization schedule for mortgages and auto loans."
    },
    "salary-to-hourly-rate.md": {
        "title": "Salary to Hourly Calculator",
        "description": "Convert your annual salary into an accurate hourly rate to value your time."
    },
    "savings-goal-planner.md": {
        "title": "Savings Goal Planner",
        "description": "Plan your monthly savings required to hit a specific financial target."
    },
    "what-is-an-expense-ratio.md": {
        "title": "Investment Fee Calculator",
        "description": "See how expense ratios and mutual fund fees impact your long-term returns."
    },
    "what-is-apr-vs-apy.md": {
        "title": "APR vs APY Converter",
        "description": "Convert nominal APR to effective APY based on compounding frequency."
    },
    "what-is-dollar-cost-averaging.md": {
        "title": "Dollar-Cost Averaging Calculator",
        "description": "Simulate a DCA strategy with regular monthly investments."
    }
}

for filename, data in updates.items():
    filepath = os.path.join("articles", filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    content = re.sub(r'title: ".*?"', f'title: "{data["title"]}"', content, count=1)
    content = re.sub(r'description: ".*?"', f'description: "{data["description"]}"', content, count=1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated titles and descriptions.")
