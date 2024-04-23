from flask import Blueprint, render_template

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
