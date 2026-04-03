import datetime
import os
import random
import re

from flask import Flask

app = Flask(__name__)

CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']

CAT_BREEDS = [
    'корниш-рекс',
    'русская голубая',
    'шотландская вислоухая',
    'мейн-кун',
    'манчкин',
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


def load_book_words(book_path):
    with open(book_path, encoding='utf-8') as book:
        text = book.read()
    return re.findall(r'[а-яА-ЯёЁa-zA-Z]+', text)


BOOK_WORDS = load_book_words(BOOK_FILE)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return ', '.join(CARS)


@app.route('/cats')
def cats():
    return random.choice(CAT_BREEDS)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    return random.choice(BOOK_WORDS)


@app.route('/counter')
def counter_page():
    counter_page.visits += 1
    return str(counter_page.visits)


counter_page.visits = 0


if __name__ == '__main__':
    app.run(debug=True)
