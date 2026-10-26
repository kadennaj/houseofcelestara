# House of Celestara by Zara

The new House of Celestara website: a responsive landing page and an interactive mock booking experience.

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
- About and Contact navigate to sections on the new landing page. Every Book now link opens the local `booking.html` page. The healing-detail link opens that page with Intuitive Healing Experiences preselected. Phone, email, and social links remain actionable.
- The outdated Squarespace attribution has been removed. There are no legacy website URLs in deployed HTML, CSS, or JavaScript.

## Design

Apple-inspired restrained typography, system fonts, generous spacing, rounded image surfaces, large photography, a sticky navigation bar, and small purposeful transitions. The original ocean image and celestial identity inform the design.

Color roles: ivory `#f9f8f5` background, deep blue-green `#203b43` primary text, muted `#53666b` secondary text, `#244d51` actions, pale lavender `#eeedf2` mission/vision surface, and gold `#8a783f` decoration. Body text is 17px on desktop and 16px in the mobile introduction, with smaller supporting text and a responsive display scale.

Desktop: header → full-width ocean hero → two-column welcome → mission/vision pair → portrait/profile pair → two-column offering grid → testimonials → horizontal photo gallery → closing quote → contact/disclaimer.

Phone: compact menu → responsive ocean hero → the same sections in a single column → touch-friendly gallery and modal.

Interactions: mobile menu with Escape support, anchor navigation, nine-slide manual testimonial carousel, horizontally scrolling gallery, image dialog with arrow keys/Escape/focus return, and native disclaimer disclosure. Motion respects `prefers-reduced-motion`; navigation opacity respects reduced transparency. Text and content remain available without animation support.

## Mock booking

The booking flow is a browser-only demo. It offers the four existing experiences, a preferred date, explicitly labeled sample times in Toronto time, and name/email/optional notes. It validates each step, supports going back without losing entries, and displays a preview summary. It does not submit, store, email, charge, or reserve anything. Reloading clears the form.

Checked the complete flow in the browser, including required experience validation, date/time selection, details, preview summary, and mobile overflow. Original asset provenance remains archived in `site-source/`; it is not part of the deployed `dist` directory.
