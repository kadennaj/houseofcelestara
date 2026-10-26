const form = document.querySelector('#booking-form');
const steps = [...form.querySelectorAll('[data-step]')];
const progress = [...document.querySelectorAll('.booking-progress li')];
const next = document.querySelector('#booking-next');
const back = document.querySelector('#booking-back');
const error = document.querySelector('#booking-error');
const dateInput = document.querySelector('#booking-date');
const result = document.querySelector('#booking-result');
let currentStep = 0;

const todayParts = new Intl.DateTimeFormat('en-CA', {timeZone: 'America/Toronto', year:'numeric', month:'2-digit', day:'2-digit'}).formatToParts(new Date());
const part = type => todayParts.find(p => p.type === type).value;
dateInput.min = `${part('year')}-${part('month')}-${part('day')}`;

function selected(name) { return form.querySelector(`input[name="${name}"]:checked`); }
function experienceName() { return selected('experience')?.closest('label').querySelector('strong').textContent; }
function dateName() { return dateInput.value ? new Intl.DateTimeFormat('en-CA',{weekday:'short',month:'short',day:'numeric',year:'numeric'}).format(new Date(`${dateInput.value}T12:00:00`)) : ''; }
function updateSummary() {
  document.querySelector('#summary-experience').textContent = experienceName() || 'Choose an offering';
  document.querySelector('#summary-when').textContent = [dateName(), selected('time')?.value].filter(Boolean).join(' · ') || 'Choose a preferred time';
}
function goToStep(index, focus = true) {
  currentStep = index;
  result.hidden = true;
  form.hidden = false;
  steps.forEach((step, i) => { step.hidden = i !== index; step.disabled = i !== index; });
  progress.forEach((item, i) => { if (i === index) item.setAttribute('aria-current','step'); else item.removeAttribute('aria-current'); });
  next.replaceChildren(document.createTextNode(index === 2 ? 'Preview booking ' : 'Continue '));
  const arrow = document.createElement('span'); arrow.setAttribute('aria-hidden','true'); arrow.textContent='→'; next.append(arrow);
  back.hidden = index === 0;
  error.hidden = true;
  if (focus) { const heading = steps[index].querySelector('legend'); heading.tabIndex = -1; heading.focus(); }
  updateSummary();
}
function validStep() {
  if (currentStep === 0 && !selected('experience')) {
    error.textContent = 'Choose an experience to continue.'; error.hidden = false; form.querySelector('[name=experience]').focus(); return false;
  }
  if (currentStep === 1 && (!dateInput.value || !dateInput.validity.valid || !selected('time'))) {
    error.textContent = 'Choose a date today or later and a sample time.'; error.hidden = false;
    if (!dateInput.value || !dateInput.validity.valid) dateInput.focus(); else form.querySelector('[name=time]').focus(); return false;
  }
  if (currentStep === 2) {
    const name = document.querySelector('#booking-name');
    name.setCustomValidity(name.value.trim() ? '' : 'Enter a name for this preview.');
    if (!form.reportValidity()) return false;
  }
  error.hidden = true;
  return true;
}
function showResult() {
  const list = document.querySelector('#result-details'); list.replaceChildren();
  const values = [['Experience',experienceName()],['Preferred date & time',`${dateName()} · ${selected('time').value} · Toronto time`],['Name',document.querySelector('#booking-name').value.trim()],['Email',document.querySelector('#booking-email').value.trim()]];
  const note = document.querySelector('#booking-notes').value.trim(); if (note) values.push(['Your note',note]);
  values.forEach(([label,value]) => { const row=document.createElement('div'),term=document.createElement('dt'),description=document.createElement('dd'); term.textContent=label; description.textContent=value; row.append(term,description); list.append(row); });
  form.hidden=true; result.hidden=false; progress.forEach(item=>item.removeAttribute('aria-current')); document.querySelector('#result-title').focus();
}
form.addEventListener('submit', event => { event.preventDefault(); if (!validStep()) return; if (currentStep < 2) goToStep(currentStep + 1); else showResult(); });
form.addEventListener('change', () => { updateSummary(); error.hidden=true; });
document.querySelector('#booking-name').addEventListener('input', event=>event.target.setCustomValidity(''));
back.addEventListener('click',()=>goToStep(currentStep-1));
document.querySelector('#edit-booking').addEventListener('click',()=>goToStep(2));
document.querySelector('#restart-booking').addEventListener('click',()=>{form.reset();document.querySelector('#result-details').replaceChildren();goToStep(0);});
const preselected = new URLSearchParams(location.search).get('experience');
const matching = [...form.querySelectorAll('[name=experience]')].find(input=>input.value===preselected);
if (matching) matching.checked=true;
goToStep(0,false);
