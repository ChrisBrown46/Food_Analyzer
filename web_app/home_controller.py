import logging

from flask import Flask
from flask import render_template

from scraper import scrape_wikipedia


app = Flask(__name__)
logger = logging.getLogger('logger')


@app.route('/', methods = ['GET', 'POST'])
def hello_world(food = 'clam_chowder'):
    additional_information = (scrape_wikipedia('https://en.wikipedia.org/wiki/' + food))
    return render_template('home.html',
                           additionalInformation = additional_information)


if __name__ == '__main__':
    app.run()
