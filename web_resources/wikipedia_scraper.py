import wikipedia

from annotations import return_errors_as_empty_string


@return_errors_as_empty_string
def scrape_wikipedia(item):
    return wikipedia.summary(item)
