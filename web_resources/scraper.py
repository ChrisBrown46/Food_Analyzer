import logging

import requests
from google import search
from selenium import webdriver


logger = logging.getLogger('logger')
driver = webdriver.PhantomJS(
    executable_path = '../phantomjs-2.1.1-windows/bin/phantomjs.exe',
    service_log_path = '../logs/ghostdriver.log',
    service_args = ['--ignore-ssl-errors=true']
)


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
