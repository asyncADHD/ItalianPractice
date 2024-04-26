from flask import Blueprint, render_template, jsonify, current_app
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


@main.route('/get-verbs-easy')
def get_verbs_easy():
    all_verbs = Verb.query.all()
    random_verb = random.choice(all_verbs) if all_verbs else None

    if random_verb:
        conjugations = random_verb.conjugations
        current_app.logger.debug(f"Fetched conjugations: {conjugations}")  # Debugging output
        return jsonify(conjugations)
    else:
        current_app.logger.debug("No verbs found in the database")  # Debugging output
        return jsonify({})


@main.route('/verbs-easy')
def verbs_easy():
    random_verb = Verb.query.order_by(func.random()).first()
    return render_template('verbs_easy.html', verb=random_verb)



