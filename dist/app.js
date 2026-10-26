const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (!reduceMotion.matches && 'IntersectionObserver' in window) {
  document.documentElement.classList.add('js-motion');
  const observer = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); } }), {threshold: 0.08});
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

const reviews = Array.from(document.querySelectorAll('.testimonial'));
const dots = Array.from(document.querySelectorAll('[data-review]'));
let reviewIndex = 0;
function showReview(index) {
  reviewIndex = (index + reviews.length) % reviews.length;
  reviews.forEach((review, i) => { review.hidden = i !== reviewIndex; });
  dots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === reviewIndex)));
  document.querySelector('.review-count').textContent = `${String(reviewIndex + 1).padStart(2, '0')} / ${String(reviews.length).padStart(2, '0')}`;
}
document.querySelector('#review-prev').addEventListener('click', () => showReview(reviewIndex - 1));
document.querySelector('#review-next').addEventListener('click', () => showReview(reviewIndex + 1));
dots.forEach(dot => dot.addEventListener('click', () => showReview(Number(dot.dataset.review))));

const gallery = document.querySelector('.gallery-track');
const imageButtons = Array.from(document.querySelectorAll('.gallery-item'));
function moveGallery(direction) {
  gallery.scrollBy({left: direction * (imageButtons[0].getBoundingClientRect().width + (window.innerWidth > 760 ? 20 : 14)), behavior: reduceMotion.matches ? 'instant' : 'smooth'});
}
document.querySelector('#gallery-prev').addEventListener('click', () => moveGallery(-1));
document.querySelector('#gallery-next').addEventListener('click', () => moveGallery(1));

const lightbox = document.querySelector('#lightbox');
let imageIndex = 0;
let returnFocus = null;
function showImage(index) {
  imageIndex = (index + imageButtons.length) % imageButtons.length;
  const item = imageButtons[imageIndex];
  const image = lightbox.querySelector('img');
  image.src = item.dataset.image;
  image.alt = item.querySelector('img').alt;
  lightbox.querySelector('.lightbox-count').textContent = `${imageIndex + 1} / ${imageButtons.length}`;
}
imageButtons.forEach((button, i) => button.addEventListener('click', () => {
  returnFocus = button; showImage(i); lightbox.showModal(); document.body.classList.add('modal-open');
}));
lightbox.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
lightbox.querySelector('.lightbox-prev').addEventListener('click', () => showImage(imageIndex - 1));
lightbox.querySelector('.lightbox-next').addEventListener('click', () => showImage(imageIndex + 1));
lightbox.addEventListener('keydown', event => { if (event.key === 'ArrowRight') { event.preventDefault(); showImage(imageIndex + 1); } if (event.key === 'ArrowLeft') { event.preventDefault(); showImage(imageIndex - 1); } });
lightbox.addEventListener('click', event => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => { document.body.classList.remove('modal-open'); returnFocus?.focus(); });

function updateGalleryControls() {
 document.querySelector("#gallery-prev").disabled = gallery.scrollLeft <= 2;
 document.querySelector("#gallery-next").disabled = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;
}
gallery.addEventListener("scroll", updateGalleryControls, {passive: true});
window.addEventListener("resize", updateGalleryControls);
updateGalleryControls();
