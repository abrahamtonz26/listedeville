# listedeville.com

Static site — no build step, no framework. Deploys to GitHub Pages.

## Deploy
1. Push this folder to a repo (e.g. `abrahamtonz/listedeville`), branch `main`.
2. Settings → Pages → Source: Deploy from branch → `main` / `(root)`.
3. Custom domain: `listedeville.com` (the `CNAME` file is already here). At your DNS: `A` records for the apex → GitHub Pages IPs (185.199.108.153 / .109 / .110 / .111) and a `CNAME` for `www` → `abrahamtonz.github.io`. Tick "Enforce HTTPS" once the cert issues.

## Update the guide
Edit `tools/new-york.md` (same checkbox format as always), then:

    python3 tools/build-data.py

That rewrites `assets/new-york.json`. Commit and push.

Price bands come from `tools/price.py` (overrides plus a category default). Occasion chips come from `tools/occasions.json` (name → occasions). Booking platforms come from `tools/platforms.py` — add a name to the right list there when a place changes platform.

## Cities live
- Seattle (`/seattle/`) — data `assets/seattle.json`
- San Francisco (`/san-francisco/`) — data `assets/san-francisco.json`
- Los Angeles (`/los-angeles/`) — data `assets/los-angeles.json`
- Chicago (`/chicago/`) — data `assets/chicago.json`
- Miami (`/miami/`) — data `assets/miami.json`
- Boston (`/boston/`) — data `assets/boston.json`; plates illustrated until photos arrive
- New York (`/new-york/`) — data `assets/new-york.json`
- Washington, DC (`/washington-dc/`) — data `assets/washington-dc.json`, occasions from `tools/occasions-washington-dc.json` (editorial assignment)

## Adding a city
1. Copy `new-york/` to `<city-slug>/` (e.g. `boston/`), delete the itineraries folder and PDF until you have them.
2. In `<city-slug>/index.html`, change the data path `/assets/new-york.json` to `/assets/<city-slug>.json`, and the heading text.
3. Put the city's markdown list at `tools/<city-slug>.md`, then run `python3 tools/build-data.py <city-slug>` (the script takes the slug; defaults to new-york).
4. Flip the city from "soon" to live in the nav (`<li class="menu">` in each page) and on the home grid. The coming-soon page for each city already exists and is linked, so nothing 404s in the meantime.
