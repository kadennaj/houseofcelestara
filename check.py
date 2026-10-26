from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path(__file__).parent
source = BeautifulSoup((root/'site-source/original.html').read_text(), 'html.parser')
page = BeautifulSoup((root/'dist/index.html').read_text(), 'html.parser')
normalize = lambda s: re.sub(r'\s+', ' ', s).strip()
output = normalize(page.get_text(' '))
nodes = source.select('main .sqs-html-content, .list-item-content__title, .list-item-content__description, footer .accordion-item__title, footer .accordion-item__description')
missing = [s for node in nodes for s in node.stripped_strings if normalize(s) not in output]
assert not missing, f'Source text missing or changed: {missing}'
assert len(page.select('.testimonial')) == 9
assert len(page.select('.offering')) == 4
assert len(page.select('.gallery-item')) == 6
assert len(page.select('h1')) == 1
for element in page.select('[src], link[href]'):
    value = element.get('src') or element.get('href')
    assert (root/'dist'/value).is_file(), f'Missing file: {value}'
for a in page.select('a[href]'):
    href = a['href']
    if href.startswith('#') and href != '#':
        assert page.find(id=href[1:]), f'Missing anchor: {href}'
    elif not href.startswith('#'):
        assert href.startswith(('https://', 'mailto:', 'tel:')), f'Invalid destination: {href}'
print(f'PASS: {len(nodes)} source content groups retain every original text fragment; 4 offerings, 9 testimonials, 6 gallery images; all local files and anchor destinations exist.')
