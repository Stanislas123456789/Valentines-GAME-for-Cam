from flask import Blueprint, render_template

main = Blueprint('mon_app', __name__, static_folder='static')


@main.route('/')
def index():
    return render_template('game.html')