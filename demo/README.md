# Demo and Screenshots

This folder contains demonstration material for the submission. Include screenshots and short descriptions that help reviewers quickly verify the system.

What to include
- `screenshot_green_ui.png` — Green Agent UI (http://localhost:8001) showing evaluation panel and results.
- `screenshot_purple_ui.png` — Purple Agent UI (http://localhost:8000) showing problem/solution flow.
- `run_demo.md` — step-by-step reproduction of a short demo run.

How to add screenshots
1. Run the services: `docker-compose up --build -d`
2. Open the UIs and take screenshots.
3. Copy PNGs into this `demo/` directory and update `run_demo.md` explaining which image corresponds to which step.

Example quick demo (run_demo.md):

```md
1. Start services: `docker-compose up --build -d`
2. Open Purple: http://localhost:8000 — submit problem "Resolver: 3+4" and view solution.
3. Open Green: http://localhost:8001 — run a 3-problem evaluation against `http://app:8000`.
4. Observe results and capture screenshots.
```
