import logging

from flask import Flask
from flask import render_template

from scraper import get_nutrition_info
from scraper import scrape_wikipedia


app = Flask(__name__)
logger = logging.getLogger('logger')


@app.route('/', methods = ['GET', 'POST'])
def hello_world(food = 'clam_chowder'):
    nutrition_info = get_nutrition_info(food)
    additional_information = scrape_wikipedia(food)
    get_nutrition_info(food)
    return render_template('home.html',
                           nutrition_info = nutrition_info,
                           additionalInformation = additional_information)


if __name__ == '__main__':
    app.run()
