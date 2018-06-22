import re

import cleaner
import scraper
from annotations import return_errors_as_empty_string


def get_nutrition_info(food):
    link = scraper.get_google_result("self nutrition data " + food)
    page_text = scraper.get_website_html(link)
    page_text = cleaner.strip_html(page_text)
    page_text = cleaner.strip_whitespace(page_text)
    nutrition_list = get_self_nutrition_page_text(page_text)

    return nutrition_list


# TODO: Use a HTML Parser
@return_errors_as_empty_string
def get_self_nutrition_page_text(page_text):
    nutrition_list = []

    regex = r"DVCalories(.+?)\D.+?\)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Calories | " + results.group(2))
    page_text = page_text[
                results.span()[0]:
                ]  # Trim the page to speed up the remaining regex's

    regex = r"DVProtein(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Protein | " + results.group(2))

    regex = r"DVTotalFat(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Total Fat | " + results.group(2))

    regex = r"DVTotalFat.+?SaturatedFat(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Saturated Fat | " + results.group(2))

    regex = r"DVCholesterol(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Cholesterol | " + results.group(2))

    regex = r"DVTotalCarbohydrate(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Carbohydrates | " + results.group(2))

    regex = r".+?Sodium(.+?g)(.+?%)"
    results = re.search(regex, page_text, re.S)
    nutrition_list.append(results.group(1) + " Sodium | " + results.group(2))

    regex = r"Sugars(~|.+?g)"
    results = re.search(regex, page_text, re.S)
    sugar_information = results.group(1)
    if sugar_information == "~":
        nutrition_list.append("No Sugars")
    else:
        nutrition_list.append(sugar_information + " Sugars")

    return nutrition_list
