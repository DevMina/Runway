# Runway ✈️

A salary and spending tracker that shows how far your money will stretch each month. Installable as a PWA — works offline, addable to your home screen. All data stays local in your browser; nothing is sent to a server.

**Live demo:** _add your GitHub Pages URL here once deployed_

## Features

- Set your monthly salary — it carries forward automatically until you change it
- Log expenses and extra income (bonuses, refunds) with category, note, and date
- Dashboard: remaining balance, spend progress bar, suggested daily budget for the rest of the month
- Category breakdown as a donut chart + legend
- Browse past and future months
- Add custom categories on the fly
- Fully offline-capable once installed

## Play / use locally

Just open `index.html` in a browser. No build step, no dependencies.

Note: the service worker (offline support) only activates over `https://` or `http://localhost` — opening the file directly (`file://`) still works, just without offline caching or the install prompt.

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `runway`) and push everything in this folder to it:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/runway.git
   git push -u origin main
   ```

2. On GitHub, go to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Set branch to `main` and folder to `/ (root)`, then save.
5. Your site will be live at:

   ```
   https://<your-username>.github.io/runway/
   ```

## Project structure

```
runway/
├── index.html          # the app (HTML + CSS + JS, single file)
├── manifest.json        # PWA metadata (name, icons, theme color)
├── service-worker.js    # offline caching
├── icons/                # app icons at all required sizes
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── icon-512-maskable.png
│   ├── apple-touch-icon.png
│   └── favicon-32.png
├── make_icons.py         # regenerate icons if you want a different design
└── README.md
```

All paths inside `index.html` and `manifest.json` are relative, so this also works fine deployed into a subfolder rather than repo root.

## Data & privacy

All transactions, salary history, and custom categories are stored in `localStorage` in the visiting browser only. There's no backend, no account, and no sync between devices — clearing browser data or switching browsers will lose the data. If you want cross-device sync later, that would need a small backend or a sync service layered on top.

## Customizing

- **Categories:** edit `DEFAULT_CATEGORIES` in `index.html`, or add custom ones in-app via the "＋ New" chip.
- **Currency symbol:** change the `CURRENCY` constant near the top of the script in `index.html`.
- **Colors/branding:** CSS custom properties are at the top of the `<style>` block in `index.html`.
- **App icon:** edit and rerun `make_icons.py` (requires `pip install pillow`), or swap in your own PNGs at the same sizes.

## License

Use it, remix it, ship it — no restrictions.
