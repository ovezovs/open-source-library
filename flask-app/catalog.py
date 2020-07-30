import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from pymongo import MongoClient
from bson.json_util import dumps
import os
from dotenv import load_dotenv
load_dotenv()

bp = Blueprint('catalog', __name__, url_prefix='/catalog')

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

# connect to the collections
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]


@bp.route('/books', methods=('GET', 'POST'))
def populate_books():
    cursor = books.find()
    books_list = list(cursor)

    return render_template('catalog/resources.html', resources=books_list, books=True)

@bp.route('/articles', methods=('GET', 'POST'))
def populate_articles():
    cursor = articles.find()
    articles_list = list(cursor)

    return render_template('catalog/resources.html', resources=articles_list, articles=True)

@bp.route('/courses', methods=('GET', 'POST'))
def populate_courses():
    cursor = courses.find()
    courses_list = list(cursor)

    return render_template('catalog/resources.html', resources=courses_list, courses=True)

@bp.route('/tracks', methods=('GET', 'POST'))
def populate_tracks():
    cursor = tracks.find()
    tracks_list = list(cursor)

    return render_template('catalog/resources.html', resources=tracks_list, tracks=True)


@bp.route('/save', methods=('GET', 'POST'))
def save_resource():
    pass