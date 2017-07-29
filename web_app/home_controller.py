import logging

from flask import Flask
from flask import render_template

from nutrition_scraper import get_nutrition_info
from wikipedia_scraper import scrape_wikipedia


app = Flask(__name__)
logger = logging.getLogger('logger')


def reformat_food(food):
    split_food = food.split('_')
    food = ''
    for piece in split_food:
        food += piece.capitalize() + ' '

    return food + '100g | %DV'


def parse_nutrition_info(food):
    nutrition_list = get_nutrition_info(food)
    food = reformat_food(food)
    calories = nutrition_list[0]
    nutrition_list = nutrition_list[1:]

    return food, calories, nutrition_list


@app.route('/', methods = ['GET', 'POST'])
def execute(food = 'chicken_pot_pie'):
    additional_information = scrape_wikipedia(food)
    food, calories, nutrition_info = parse_nutrition_info(food)
    return render_template('home.html',
                           food = food,
                           calories = calories,
                           nutrition_info = nutrition_info,
                           additionalInformation = additional_information)


if __name__ == '__main__':
    print('Starting web app...')
    app.run()
