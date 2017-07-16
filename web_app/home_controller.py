from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/handle_data', methods = ['POST'])
def handle_data():
    print(request.form['Name'])
    return render_template('home.html')


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
