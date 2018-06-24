import requests
from googlesearch import search

from annotations import return_errors_as_empty_string


@return_errors_as_empty_string
def get_google_result(query):
    for url in search(query, stop=1):
        return url


@return_errors_as_empty_string
def get_website_text(link):
    return requests.get(link, timeout=2).text
