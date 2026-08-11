# Personal Finance Content Site — Automated SEO Site Builder

Automated pipeline: seed keywords → AI-generated educational/comparison
articles → static HTML site → git-based free hosting → AdSense monetization.

## Why this shape

- **Educational/comparison angle, not prescriptive advice.** Personal
  finance is a "YMYL" (Your Money Your Life) category in Google's ranking
  systems — it gets extra scrutiny, and pure AI-generated "you should do X
  with your money" content both ranks poorly and carries real liability
  risk if read as financial advice. Sticking to explaining concepts and
  comparing options (not telling readers what to do) is safer on both
  fronts. Every generated article includes a disclaimer to this effect —
  don't remove it.
- **Static site, not WordPress** — free hosting via GitHub Pages or
  Cloudflare Pages, git-based publishing, effectively $0 to run until
  there's enough traffic to matter.
- **AdSense over affiliate** — no platform API dependency risk (learned
  from the Shopee attempt). AdSense does require: an approved application,
  a minimum content/traffic bar, and a live domain — factor that lead time
  in before expecting revenue.

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add ANTHROPIC_API_KEY
```

### Content generation (needs Anthropic API key)
```bash
python content_gen.py --count 3   # generates 3 articles from keywords.csv
```
Generated articles land in `articles/*.md` with frontmatter (title, meta
description, slug, keyword). `keywords.csv` tracks a `used` column so the
same keyword isn't regenerated — check it in periodically to add more
seed keywords.

### Build the static site
```bash
python site_builder.py   # converts articles/*.md -> public/*.html
```
Outputs to `public/` — this is what you deploy.

### Publish
```bash
python publish.py   # git add/commit/push public/ to your Pages branch
```
Requires the repo to already be connected to GitHub Pages or Cloudflare
Pages (one-time manual setup — see "Hosting setup" below).

### Run the full cycle
```bash
python main.py --once --count 2   # generate 2 new articles, rebuild, publish
```

## Hosting setup (one-time, manual)

1. Create a GitHub repo, push this project.
2. **GitHub Pages**: Settings → Pages → deploy from `public/` folder on
   your main branch (or a dedicated `gh-pages` branch — adjust
   `publish.py` if so).
   **OR Cloudflare Pages**: connect the repo, set build output directory
   to `public/`. Slightly better performance/analytics than GitHub Pages,
   still free tier.
3. Point a custom domain at it if you want (optional, ~$10-15/year — this
   is the one cost worth spending on early since domain age helps SEO and
   a custom domain is required for AdSense approval in most cases).

## AdSense

1. Apply at https://adsense.google.com once the site has some real content
   live (10+ articles is a reasonable starting bar, though Google doesn't
   publish an exact minimum).
2. Once approved, drop your AdSense snippet into `templates/base.html`
   where marked, and add the `ads/ads.txt` verification file content
   AdSense gives you.
3. Approval can take days to weeks and isn't guaranteed on first try —
   budget for that lag before counting on revenue.

## Scheduling

GitHub Actions scheduled workflow (free) is the natural fit since you're
already git-publishing. Example: 2x/week article generation + publish.
See `.github/workflows/publish.yml` for a starter workflow (uses repo
secrets for `ANTHROPIC_API_KEY`).

## Content quality notes for whoever (human or agent) maintains this

- Keep the disclaimer block in every article — it's both an honesty
  practice and a real risk-reducer.
- Favor "explain X" and "X vs Y" framing over "you should do X."
- Internal linking between articles helps SEO — `site_builder.py` has a
  basic related-articles block; expanding this over time is worth the
  effort as the article count grows.
- Real revenue here is a slow-burn (months, not weeks) — SEO content sites
  compound but take time to rank. Don't expect early traffic.
