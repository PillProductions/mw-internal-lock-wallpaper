# mw-internal-lock-wallpaper

Rotate Intune lock screen wallpaper using a GitHub Pages-hosted JPEG URL, without a backend.

## Why this approach

GitHub Pages is static hosting, so it cannot generate a truly random server response per request.

For Intune, the reliable pattern is:

1. Keep all source images in `images/`.
2. Use GitHub Actions to periodically pick one random image.
3. Publish it as a single file: `wallpaper.jpg`.
4. Point Intune to that direct JPEG URL.

This gives you a direct image URL (no HTML output), and the image rotates automatically.

## Repository layout

- `images/` Source `.jpg` / `.jpeg` files.
- `scripts/pick_wallpaper.py` Chooses a random source image and copies it to `wallpaper.jpg`.
- `.github/workflows/rotate-wallpaper.yml` Runs every 2 hours (and manually) to rotate `wallpaper.jpg`.
- `wallpaper.jpg` The file Intune should use.

## Setup

1. Upload your JPEGs into `images/`.
2. Enable GitHub Pages for this repository (deploy from `main`, root).
3. Run the workflow once manually from Actions: **Rotate wallpaper**.
4. Use this URL in Intune:

	`https://<your-github-pages-domain>/wallpaper.jpg`

Examples:

- `https://pillproductions.github.io/mw-internal-lock-wallpaper/wallpaper.jpg`
- `https://wallpaper.example.com/wallpaper.jpg` (if using a custom domain)

## Optional browser-only random redirect

`random.html` contains a JavaScript redirect that picks an image from a hardcoded list.
This is only for browser testing and not recommended for Intune policy URL usage.

If you use it, keep the image list in `random.html` updated.

