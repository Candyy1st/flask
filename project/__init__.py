import requests
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    # news_list = requests.get('http://localhost:5000/api/news/')
    # news_list = news_list.json()
    # news_list = sorted(news_list, key=lambda k: k['created_at'], reverse=True)

    categories = requests.get('http://localhost:8000/categories/')
    categories = categories.json()

    return render_template('index.html', categories=categories)

@app.route('/categories/<id>')
def categories(id):
    news_list = requests.get('http://localhost:8000/news/')
    news_list = news_list.json()

    categories = requests.get('http://localhost:8000/categories/')
    categories = categories.json()

    by_category = []
    for i in news_list:
        if i['category'] == int(id):
            by_category.append(i)

    return render_template('index.html, news_list=by_category, categories=categories')