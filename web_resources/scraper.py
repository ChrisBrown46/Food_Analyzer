import requests
from googlesearch import search
from selenium import webdriver

from annotations import return_errors_as_empty_string

driver = webdriver.PhantomJS(
    executable_path="../phantomjs-2.1.1-windows/bin/phantomjs.exe",
    service_log_path="../logs/ghostdriver.log",
    service_args=["--ignore-ssl-errors=true"],
)


@return_errors_as_empty_string
def get_google_result(query):
    for url in search(query, stop=1):
        return url


@return_errors_as_empty_string
def get_website_html(link):
    driver.get(link)
    return driver.execute_script(
        "return document.getElementsByTagName('html')[0].innerHTML"
    )


@return_errors_as_empty_string
def get_website_text(link):
    return requests.get(link, timeout=2).text
