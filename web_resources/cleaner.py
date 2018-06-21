import re


def strip_whitespace(page_text):
    regex = r"(\s)"
    return re.sub(regex, "", page_text)


def strip_html(page_text):
    regex = r"<(.+?)>"
    intermediate_text = re.sub(regex, "", page_text)
    regex = r"&nbsp;"
    return re.sub(regex, "", intermediate_text)


def strip_reference_blocks(page_text):
    regex = r"\[\d\]"
    return re.sub(regex, "", page_text)


def strip_newlines(page_text):
    regex = r"\n"
    return re.sub(regex, " ", page_text)
