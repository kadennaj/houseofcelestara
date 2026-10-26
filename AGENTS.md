# Project instructions

- Hosting target: Vercel. Do not create or publish a ChatGPT Sites deployment.
- The user manages publication on Vercel unless they explicitly ask the agent to deploy.
- Preserve the original House of Celestara copy, brand labels, offerings, testimonials, and contact facts. Do not add marketing claims or filler copy.
- `dist/` is the complete deployable static site. No runtime dependencies or environment variables are required.
- Keep original asset URLs and content provenance in `site-source/`.
- After content edits, run `python3 check.py`; after JavaScript edits, run `node --check dist/app.js`.
