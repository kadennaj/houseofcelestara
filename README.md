# House of Celestara by Zara

A responsive, buildless landing page reconstructed from the live source at https://www.houseofcelestara.com/ on October 26, 2026.

## Preview

Run `python3 -m http.server 4173 --bind 127.0.0.1 --directory dist`, then open http://127.0.0.1:4173/.

The `dist` directory is the deployable website. It has no framework, package installation, or external font dependency. `build.py` generates its HTML from the captured original page; it requires Beautiful Soup. `check.py` verifies source text retention, original offerings and testimonials, local asset paths, and internal anchors. CSS and JavaScript are edited directly in `dist`.

## Deploy on Vercel

Import the `kadennaj/houseofcelestara` GitHub repository into Vercel. Use the repository root as the Root Directory. The included `vercel.json` selects the Other framework preset, skips installation/build commands, and serves the committed `dist` directory. No environment variables are needed.

Vercel does not run the optional Python content tools. The finished HTML, CSS, JavaScript, and all images are already committed. Publish from your Vercel account when ready.

## Source and content

- `site-source/original.html`: original landing-page HTML.
- `site-source/content.json`: extracted original copy and all nine testimonials.
- `site-source/assets.json`: source URL for every downloaded asset.
- Ten original assets are hosted locally, including the original logo, ocean photograph, Zara portrait, candle/cacao still life, and six gallery photographs.
- Original marketing copy, four offerings, professional labels, testimonials, contact information, social handles, and disclaimer are retained. Layout, hierarchy, decorative marks, accessibility descriptions, and interaction controls are new.
- About, Contact/Book now, the healing-detail link, Google reviews, and social destinations point to the original external destinations. Phone and email are actionable.
- The original Squarespace attribution is retained as source copy.

## Design

Apple-inspired restrained typography, system fonts, generous spacing, rounded image surfaces, large photography, a sticky navigation bar, and small purposeful transitions. The original ocean image and celestial identity inform the design.

Color roles: ivory `#f9f8f5` background, deep blue-green `#203b43` primary text, muted `#53666b` secondary text, `#244d51` actions, pale lavender `#eeedf2` mission/vision surface, and gold `#8a783f` decoration. Body text is 17px on desktop and 16px in the mobile introduction, with smaller supporting text and a responsive display scale.

Desktop: header → full-width ocean hero → two-column welcome → mission/vision pair → portrait/profile pair → two-column offering grid → testimonials → horizontal photo gallery → closing quote → contact/disclaimer.

Phone: compact menu → responsive ocean hero → the same sections in a single column → touch-friendly gallery and modal.

Interactions: mobile menu with Escape support, anchor navigation, nine-slide manual testimonial carousel, horizontally scrolling gallery, image dialog with arrow keys/Escape/focus return, and native disclaimer disclosure. Motion respects `prefers-reduced-motion`; navigation opacity respects reduced transparency. Text and content remain available without animation support.

## Access limitations

The public landing page and its image CDN were accessible. About, Contact, and healing-detail pages returned HTTP 200. The site's booking/contact form remains on the original website; no form submission or purchase was performed. This project does not recreate the site's backend or additional pages. Ownership and third-party licensing of source assets have not been independently verified; source URLs are retained for review.
