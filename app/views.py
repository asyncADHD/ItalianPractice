from flask import Blueprint, render_template, jsonify
import random
from sqlalchemy import func
from .models import Verb

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/conjugation-start')
def conjugation_start():
    return render_template('conjugation_start.html')


@main.route('/select-difficulty')
def select_difficulty():
    return render_template('select_difficulty.html')


@main.route('/practice/<difficulty>')
def practice(difficulty):
    return render_template('practice.html', difficulty=difficulty)


@main.route('/verbs-easy')
def verbs_easy():
    random_verb = Verb.query.order_by(func.random()).first()
    print(random_verb)
    return render_template('verbs_easy.html', verb=random_verb)


@main.route('/get-verb')
def get_verb():
    random_verb = Verb.query.order_by(func.random()).first()
    return jsonify(verb=random_verb if random_verb else "No verb found")
