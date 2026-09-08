import os

files = {
    "about.md": '''---
title: "About Money Clarity Tools"
description: "Why we built a free, independent suite of financial calculators and analytical tools."
slug: "about"
path: "about"
---

## About Money Clarity Tools

Money Clarity is an independent suite of free, interactive financial calculators and quantitative tools. 

We believe that personal finance decisions - whether it is paying off debt, saving for an emergency, or analyzing an investment portfolio - should be driven by hard numbers, not sales pitches.

Too many financial tools on the internet are disguised lead-generation forms for credit cards or expensive financial advisors. We built this platform to provide clean, ad-supported, math-first utilities that anyone can use without handing over their personal data.

### Who Built This?
This tool suite is maintained by **Ray Porter**, an independent quantitative financial researcher and software developer. Ray combines background knowledge in data analysis and software engineering to create transparent, accurate, and easy-to-use financial models.

### Our Approach
Every calculator on this site is built on standard mathematical formulas for compounding, amortization, and valuation. We aim to expose the underlying math so you can make informed decisions. We do not offer personalized financial advice.

If you find a bug in any of our calculators or want to request a new tool, please [contact us](contact.html).
''',
    "disclaimer.md": '''---
title: "Disclaimer"
description: "Important disclaimer regarding the use of Money Clarity financial calculators."
slug: "disclaimer"
path: "disclaimer"
---

## Financial Disclaimer

The interactive calculators, tools, and data provided on **Money Clarity** are for educational and informational purposes only. They do not constitute financial, investment, legal, or tax advice.

### No Guarantee of Accuracy
While we strive to ensure the formulas and outputs of our calculators are mathematically accurate, we make no warranties or representations regarding their precision or applicability to your specific financial situation. Users should verify all calculations and data independently before making any financial decisions.

### Not Financial Advice
The creator of this platform, Ray Porter, is not a registered financial advisor, broker, or tax professional. The tools provided simulate scenarios based on user inputs and standard financial formulas. They should not replace consultations with qualified professionals.

### Investment Risks
Any tools dealing with investing (such as the IDX Stock Screener, Dollar-Cost Averaging calculator, or Expense Ratio calculator) rely on historical data or user-provided estimates. Past performance is not indicative of future results. All investments carry risk, including the possible loss of principal.

By using this software, you agree that Money Clarity and its creators are not liable for any financial losses or damages resulting from the use of these tools.
''',
    "contact.md": '''---
title: "Contact Support"
description: "Get in touch with Money Clarity for calculator bug reports, feature requests, or inquiries."
slug: "contact"
path: "contact"
---

## Contact Us

Have a feature request, found a bug in one of our calculators, or want to report an issue with the site? We'd love to hear from you.

### Email
You can reach out to us directly at:
**[contact@moneyclarity.blog](mailto:contact@moneyclarity.blog)**

### What to include in a bug report
If a calculator is producing unexpected results, please include:
- The name of the calculator (e.g., Debt Payoff, Compound Interest).
- The exact inputs you entered.
- What you expected to see vs. what was outputted.

We typically respond within 2-3 business days.
''',
    "privacy-policy.md": '''---
title: "Privacy Policy"
description: "Privacy policy for Money Clarity Tools."
slug: "privacy-policy"
path: "privacy-policy"
---

## Privacy Policy

At Money Clarity, your privacy is important to us. This Privacy Policy outlines how we handle data when you use our financial calculators and tools.

### 1. Client-Side Calculations
Most of the calculators on this platform run entirely in your web browser (client-side). This means the financial numbers, salaries, debt amounts, and goals you enter are **never sent to our servers** and are never stored in a database. Your data remains on your device.

### 2. Cookies and Analytics
We may use standard web analytics and advertising partners (such as Google AdSense) to keep this tool suite free to use. These third parties may use cookies, web beacons, and similar technologies to collect information about your visit.
- **Google AdSense:** Google uses cookies to serve ads based on your prior visits. You can opt out of personalized advertising by visiting Google's Ads Settings.

### 3. Contact Information
If you choose to email us or use our contact form, we will solely use your email address to respond to your inquiry. We do not sell or share your contact information with third parties.

### 4. Changes to this Policy
We reserve the right to update this Privacy Policy at any time. Any changes will be posted on this page.

*Last Updated: September 2026*
''',
    "terms-of-service.md": '''---
title: "Terms of Service"
description: "Terms of Service for Money Clarity Tools."
slug: "terms-of-service"
path: "terms-of-service"
---

## Terms of Service

By accessing or using the calculators and tools on Money Clarity, you agree to be bound by these Terms of Service.

### 1. Use of Tools
Money Clarity provides a suite of interactive financial calculators for personal, non-commercial use. You may not scrape, reverse-engineer, or systematically extract data or formulas from our site for commercial purposes.

### 2. No Warranties
The tools are provided "as is" without any warranties, express or implied. We do not guarantee the accuracy, completeness, or reliability of any outputs generated by the calculators.

### 3. Limitation of Liability
In no event shall Money Clarity or its creators be liable for any direct, indirect, incidental, or consequential damages arising out of the use or inability to use our tools. All financial decisions are made at your own risk.

### 4. Governing Law
These terms shall be governed by and construed in accordance with standard international law, without regard to conflict of law principles.

*Last Updated: September 2026*
'''
}

for filename, content in files.items():
    with open(os.path.join("articles", filename), "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated meta pages.")
