# Master Connection — Run & Deploy

Quick steps to run the static site locally and deploy.

Prerequisites
- Node.js (16+ recommended)

Local development
1. Install dependencies:

```bash
cd /d D:\Master_connection
npm install
```

2. Start dev server:

```bash
npm run dev
```

Vite will serve the site (by default at `http://localhost:5173`). Open that URL in your browser.

Build & preview

```bash
npm run build
npm run preview
```

Deploy options
- Netlify / Vercel: Connect the repository or drag-and-drop the `dist` (build) folder.
- GitHub Pages: build the site (`npm run build`) and publish the `dist` contents (use `gh-pages` or a workflow).

Notes
- The project is a static HTML/CSS site. `create_root_index.py` and `link_sidebar.py` are helper scripts and contain hardcoded Windows paths — edit their `base_dir`/`root_dir` values to `d:\\Master_connection` before running them.
