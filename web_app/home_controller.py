import logging

from flask import Flask
from flask import render_template
from flask import request

from nutrition_scraper import get_nutrition_info
from wikipedia_scraper import scrape_wikipedia

app = Flask(__name__)
logger = logging.getLogger("logger")


def reformat_food(food):
    split_food_spaces = food.split(" ")
    split_food_underlines = food.split("_")
    split_food = (
        split_food_spaces
        if len(split_food_spaces) > len(split_food_underlines)
        else split_food_underlines
    )

    food = ""
    for piece in split_food:
        food += piece.capitalize() + " "

    return food + "100g | %DV"


def parse_nutrition_info(food):
    nutrition_list = get_nutrition_info(food)
    food = reformat_food(food)
    calories = nutrition_list[0]
    nutrition_list = nutrition_list[1:]

    return food, calories, nutrition_list


@app.route("/", methods=["GET", "POST"])
def execute():
    # Only accepts the first image.
    food = "carrot cake"
    picture = request.files.get("picture", None)
    if picture is not None:
        # TODO: GENERATE FOOD ITEM BASED ON PICTURE
        food = "chocolate cake"

    additional_information = scrape_wikipedia(food)
    food, calories, nutrition_info = parse_nutrition_info(food)

    return render_template(
        "home.html",
        food=food,
        calories=calories,
        nutrition_info=nutrition_info,
        additionalInformation=additional_information,
    )


if __name__ == "__main__":
    print("Starting web app at localhost:5000")
    app.run()
