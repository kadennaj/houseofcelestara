"""Build the landing page directly from the captured source copy."""
from bs4 import BeautifulSoup
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).parent
soup = BeautifulSoup((ROOT / 'site-source/original.html').read_text(), 'html.parser')
blocks = soup.select('main .sqs-html-content')
BASE = 'https://www.houseofcelestara.com'

def text(i):
    return blocks[i].get_text('', strip=False).strip()

def content(i):
    node = BeautifulSoup(str(blocks[i]), 'html.parser')
    for el in node.find_all(True):
        el.attrs = {'href': BASE + el['href']} if el.name == 'a' and el.get('href','').startswith('/') else {}
    return node.div.decode_contents()

book = f'<a class="button" href="{BASE}/contact">Book now <span aria-hidden="true">↗</span></a>'
testimonials = []
for item in soup.select('.list-item'):
    title = item.select_one('.list-item-content__title')
    author = item.select_one('.list-item-content__description')
    if title and author:
        testimonials.append({'quote': title.get_text('',strip=False).strip(), 'author': author.get_text('',strip=False).strip()})

offerings = ''
photos = [('healing.jpg','Candle, amethyst, cacao and palo santo'),('healingcircle5.jpg','Singing bowl and cushions arranged on a lawn'),('despacho1.jpg','Zara arranging an offering outdoors'),('firepit.jpg','Sacred fire')]
for n, i in enumerate([12,14,16,18]):
    photo, alt = photos[n]
    offerings += f'''<article class="offering reveal"><div class="offering-image"><img src="assets/{photo}" alt="{alt}" loading="lazy" width="1200" height="850"></div><div class="offering-copy"><h3>{escape(text(i))}</h3>{content(i+1)}</div></article>'''

slides = ''.join(f'''<figure class="testimonial" {'hidden' if i else ''} aria-label="{i+1} of {len(testimonials)}"><blockquote>{escape(t['quote'])}</blockquote><figcaption>{escape(t['author'])}</figcaption></figure>''' for i,t in enumerate(testimonials))
gallery_data = [('healingcircle5.jpg','Singing bowl and cushions on a lawn'),('despacho5.jpg','Zara beside a tree'),('despacho1.jpg','Zara arranging an offering'),('despacho6.jpg','Hands holding a flower offering'),('firepit.jpg','Fire pit with garden seating'),('moonpic.jpg','The moon in the night sky')]
gallery = ''.join(f'''<button class="gallery-item" data-image="assets/{file}" data-index="{i}" aria-label="Open image: {alt}"><img src="assets/{file}" alt="{alt}" loading="lazy" width="800" height="1050"><span aria-hidden="true">↗</span></button>''' for i,(file,alt) in enumerate(gallery_data))
footer_items = soup.select('footer .accordion-item')
disclaimer = footer_items[1].select_one('.accordion-item__description')
clean_disclaimer = BeautifulSoup(str(disclaimer),'html.parser')
for el in clean_disclaimer.find_all(True): el.attrs = {}
google = next(a['href'] for a in soup.select('a[href]') if a.get_text(strip=True)=='Google')

html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>House of Celestara by Zara</title>
  <meta name="description" content="A sacred sanctuary for healing, ceremony, and spiritual awakening.">
  <meta name="theme-color" content="#f9f8f5">
  <meta property="og:title" content="House of Celestara by Zara">
  <meta property="og:description" content="A sacred sanctuary for healing, ceremony, and spiritual awakening.">
  <link rel="preload" href="assets/hero.jpg" as="image">
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to Content</a>
<header class="site-header"><div class="header-inner">
  <a href="#" class="wordmark" aria-label="House of Celestara by Zara"><span>House of Celestara</span><small>By Z a r a</small></a>
  <nav class="desktop-nav" aria-label="Main navigation"><a href="{BASE}/about">About</a><a href="#offerings">OFFERINGS</a><a href="{BASE}/contact">Contact</a></nav>
  <div class="header-actions">{book}<button class="menu-toggle" aria-label="Open Menu" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span></button></div>
</div><nav id="mobile-nav" class="mobile-nav" aria-label="Mobile navigation" hidden><a href="{BASE}/about">About</a><a href="#offerings">OFFERINGS</a><a href="{BASE}/contact">Contact</a><a href="https://www.instagram.com/houseofcelestarabyzara/">Instagram</a><a href="https://www.tiktok.com/@houseof.celestara">TikTok</a></nav></header>
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <img class="hero-image" src="assets/hero.jpg" alt="" fetchpriority="high" width="2500" height="1662">
    <div class="hero-wash"></div>
    <div class="hero-content">
      <div class="celestial" aria-hidden="true">✦</div>
      <h1 id="hero-title">Where the soul awakens, <br>and the stars <em>remember</em></h1>
      <p class="hero-description">A sacred sanctuary for healing, ceremony, and spiritual awakening.</p>
      {book}
    </div>
    <div class="hero-bottom"><p>You are not broken, you are sacred.<br>You are not lost, you are being called home.<br>And your soul already knows the way.</p><a class="down-link" href="#welcome" aria-label="Welcome, Beautiful Soul."><span aria-hidden="true">↓</span></a></div>
  </section>
  <section class="welcome section-wrap" id="welcome">
    <div class="welcome-heading reveal"><span class="eyebrow">House of Celestara</span><h2>Welcome, <br>Beautiful Soul.</h2><span class="small-star" aria-hidden="true">✦</span></div>
    <div class="welcome-copy reveal">{content(3)}</div>
  </section>
  <section class="purpose section-wrap">
    <div class="purpose-inner reveal"><article><span class="small-star" aria-hidden="true">✧</span><h2>{escape(text(4))}</h2>{content(5)}</article><article><span class="small-star" aria-hidden="true">☾</span><h2>{escape(text(6))}</h2>{content(7)}</article></div>
  </section>
  <section class="meet section-wrap" id="zara">
    <div class="portrait reveal"><img src="assets/zara.jpg" alt="Zara" width="1024" height="1024" loading="lazy"></div>
    <div class="meet-copy reveal"><span class="eyebrow">{escape(text(8))}</span><h2>{escape(text(10))}</h2><div class="credentials">{content(9)}</div><a class="text-link" href="{BASE}/about">About <span aria-hidden="true">↗</span></a></div>
  </section>
  <section class="offerings" id="offerings"><div class="section-wrap">
    <div class="section-heading reveal"><h2>{escape(text(11))}</h2><span class="small-star" aria-hidden="true">✦</span></div>
    <div class="offering-grid">{offerings}</div>
    <div class="center-action reveal">{book}</div>
  </div></section>
  <section class="reviews section-wrap" id="reviews"><div class="review-header reveal"><h2>See what people are saying <br>here and on <a href="{escape(google)}">Google <span aria-hidden="true">↗</span></a></h2><div class="review-controls"><button class="round-button" id="review-prev" aria-label="Previous testimonial">←</button><button class="round-button" id="review-next" aria-label="Next testimonial">→</button></div></div>
    <div class="testimonial-stage" aria-live="polite" aria-atomic="true">{slides}</div><div class="review-bottom"><span class="review-count" aria-live="polite">01 / 09</span><div class="review-dots">{''.join(f'<button aria-label="Testimonial {i+1}" aria-current="{str(i==0).lower()}" data-review="{i}"></button>' for i in range(len(testimonials)))}</div></div>
  </section>
  <section class="gallery-section"><div class="gallery-track" aria-label="Ceremony photo gallery">{gallery}</div><div class="gallery-controls section-wrap"><span class="small-star" aria-hidden="true">✧</span><div><button class="round-button" id="gallery-prev" aria-label="Previous photos">←</button><button class="round-button" id="gallery-next" aria-label="Next photos">→</button></div></div></section>
  <section class="closing section-wrap reveal"><span class="small-star" aria-hidden="true">✦</span><h2>{escape(text(20))}</h2>{book}</section>
</main>
<footer><div class="section-wrap footer-inner"><div class="footer-top"><div class="footer-brand"><img src="assets/logo.png" alt="House of Celestara" loading="lazy" width="1140" height="531"><h2>House of Celestara By Z a r a</h2><p>Intuitive Energy Healer | Spiritual Teacher &amp; Guide</p></div><div class="contact-info"><p>📍 Maple, Ontario</p><a href="mailto:houseofcelestara@gmail.com">📧 houseofcelestara@gmail.com</a><a href="tel:+14169923515">📱 416-992-3515</a><p>Follow on Instagram <a href="https://www.instagram.com/houseofcelestarabyzara/">@houseofcelestarabyzara</a> &amp; TikTok: <a href="https://www.tiktok.com/@houseof.celestara">@houseof.celestara</a></p></div></div>
  <details class="disclaimer"><summary>Disclaimer<span aria-hidden="true">+</span></summary><div>{clean_disclaimer.div.decode_contents()}</div></details>
  <div class="footer-bottom"><span>House of Celestara By Z a r a</span><p>Made with <a href="https://squarespace.com/">Squarespace</a></p></div>
</div></footer>
<dialog id="lightbox" aria-label="Ceremony photo"><button class="lightbox-close round-button" aria-label="Close image">×</button><button class="lightbox-prev round-button" aria-label="Previous image">←</button><img alt=""><button class="lightbox-next round-button" aria-label="Next image">→</button><p class="lightbox-count" aria-live="polite"></p></dialog>
</body></html>'''
(ROOT/'dist/index.html').write_text(html)
(ROOT/'site-source/content.json').write_text(json.dumps({'source':BASE,'blocks':[b.get_text('',strip=False).strip() for b in blocks],'testimonials':testimonials},ensure_ascii=False,indent=2))
print(f'Built landing page: {len(blocks)} original text blocks, {len(testimonials)} testimonials, {len(gallery_data)} gallery photos.')
