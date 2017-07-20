import logging
import re

import cleaner
import scraper


logger = logging.getLogger('logger')


def scrape_wikipedia(item):
    link = 'https://en.wikipedia.org/wiki/' + item
    page_text = scraper.get_website_text(link)
    page_text = get_wikipedia_page_text(page_text)
    page_text = cleaner.strip_html(page_text)
    page_text = cleaner.strip_reference_blocks(page_text)
    page_text = cleaner.strip_newlines(page_text)

    return page_text


def get_wikipedia_page_text(page_text):
    regex = r'<p>(.+?)<div '
    results = re.search(regex, page_text, re.S)

    try:
        return results.group(1)
    except Exception as e:
        logger.error('Could not parse wikipedia page', e)
        return ''
