# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Corporate website for Horizon Software (株式会社 Horizon Software), a fintech company. Hosted on GitHub Pages with a custom domain (`horizonsoftware.co.jp` via CNAME). The site is in Japanese.

## Architecture

Pure static site — no build step, no bundler, no framework. Files are served directly via GitHub Pages.

- `index.html` — Single-page main site with sections: hero, services, news, about, contact
- `articles/` — News article pages (e.g., `company-establishment.html`)
- `staff/` — Staff profile pages with JP/EN language toggle (noindexed). Uses `staff-styles.css` for business card styling
- `styles.css` — Main stylesheet with CSS custom properties for light/dark theming
- `script.js` — All client-side behavior: dark mode toggle (persisted to localStorage), mobile menu, particles.js config (hero + background), scroll animations, image modal, contact form (demo-only, no backend)
- `python_util/` — One-off image processing scripts (PIL-based), not part of the website itself

## Key Patterns

- **Theming**: Light/dark mode via `data-theme` attribute on `<html>` and CSS custom properties in `:root` / `html[data-theme="dark"]`. Both `styles.css` and `staff/staff-styles.css` define their own theme variables.
- **Particles**: Two particles.js instances — `#particles-js` (hero, white, interactive) and `#background-particles` (page-wide, theme-aware color, non-interactive). Colors update on theme toggle via `pJSDom`.
- **Responsive breakpoints**: 1040px, 992px, 815px (mobile nav), 576px. Height breakpoints at 850px, 760px, 680px for hero scaling.
- **Staff pages**: Language switching via `body.lang-jp`/`body.lang-en` classes toggling `.jp-content`/`.en-content` visibility.

## Development

Open `index.html` in a browser directly or use any static file server. No install or build required.

## Deployment

Push to `main` branch — GitHub Pages serves from there. The `CNAME` file maps to `horizonsoftware.co.jp`.
