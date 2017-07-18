import logging
import re

import requests


logger = logging.getLogger('logger')


def scrape_wikipedia(link):
    page_text = get_wikipedia_page_text(link)
    page_text = strip_html(page_text)
    page_text = strip_reference_blocks(page_text)
    page_text = strip_newlines(page_text)

    return page_text


def get_wikipedia_page_text(link):
    try:
        page_text = requests.get(link).text
    except Exception as e:
        logger.error('Could not find wikipedia page', e)
        return ''

    regex = r'<\/a>.<\/p>.<p>(.+?)<div id'
    results = re.search(regex, page_text, re.S)

    try:
        return results.group(1)
    except Exception as e:
        logger.error('Could not find wikipedia page', e)
        return ''


def strip_html(page_text):
    regex = r'<(.+?)>'
    return re.sub(regex, '', page_text)


def strip_reference_blocks(page_text):
    regex = r'\[\d\]'
    return re.sub(regex, '', page_text)


def strip_newlines(page_text):
    regex = r'\n'
    return re.sub(regex, ' ', page_text)
