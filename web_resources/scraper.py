import logging
import re

import requests
from google import search
from selenium import webdriver


logger = logging.getLogger('logger')
driver = webdriver.PhantomJS(
    executable_path = '../phantomjs-2.1.1-windows/bin/phantomjs.exe',
    service_log_path = '../logs/ghostdriver.log',
    service_args = ['--ignore-ssl-errors=true']
)


def scrape_wikipedia(item):
    link = 'https://en.wikipedia.org/wiki/' + item
    page_text = get_website_text(link)
    page_text = get_wikipedia_page_text(page_text)
    page_text = strip_html(page_text)
    page_text = strip_reference_blocks(page_text)
    page_text = strip_newlines(page_text)

    return page_text


def get_wikipedia_page_text(page_text):
    regex = r'<p>(.+?)<div '
    results = re.search(regex, page_text, re.S)

    try:
        return results.group(1)
    except Exception as e:
        logger.error('Could not parse wikipedia page', e)
        return ''


def get_nutrition_info(food):
    link = get_google_result('self nutrition data ' + food)
    page_text = get_website_html(link)
    page_text = strip_html(page_text)
    page_text = strip_whitespace(page_text)
    nutrition_list = get_self_nutrition_page_text(page_text)

    return nutrition_list


def get_self_nutrition_page_text(page_text):
    nutrition_list = []
    try:
        regex = r'DVCalories(.+?)\D.+?\)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Calories | ' + results.group(2))
        page_text = page_text[results.span()[0]:]  # Trim the page to speed up the remaining regex's

        regex = r'DVProtein(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Protein | ' + results.group(2))

        regex = r'DVTotalFat(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Total Fat | ' + results.group(2))

        regex = r'DVTotalFat.+?SaturatedFat(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Saturated Fat | ' + results.group(2))

        regex = r'DVCholesterol(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Cholesterol | ' + results.group(2))

        regex = r'DVTotalCarbohydrate(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Carbohydrates | ' + results.group(2))

        regex = r'%Sodium(.+?g)(.+?%)'
        results = re.search(regex, page_text, re.S)
        nutrition_list.append(results.group(1) + ' Sodium | ' + results.group(2))

        regex = r'Sugars(~|.+?g)'
        results = re.search(regex, page_text, re.S)
        if results.group(1) == '~':
            nutrition_list.append('No Sugars')
        else:
            nutrition_list.append(results.group(1) + ' Sugars')

        return nutrition_list

    except Exception as e:
        logger.error('Could not parse nutrition data', e)
        return ''


def get_google_result(query):
    for url in search(query, stop = 1):
        return url


def get_website_html(link):
    try:
        driver.get(link)
        return driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    except Exception as e:
        logger.error('Could not find web page', e)
        return ''


def get_website_text(link):
    try:
        return requests.get(link, timeout = 2).text
    except Exception as e:
        logger.error('Could not find web page page', e)
        return ''


def strip_whitespace(page_text):
    regex = r'(\s)'
    return re.sub(regex, '', page_text)


def strip_html(page_text):
    regex = r'<(.+?)>'
    intermediate_text = re.sub(regex, '', page_text)
    regex = r'&nbsp;'
    return re.sub(regex, '', intermediate_text)


def strip_reference_blocks(page_text):
    regex = r'\[\d\]'
    return re.sub(regex, '', page_text)


def strip_newlines(page_text):
    regex = r'\n'
    return re.sub(regex, ' ', page_text)
