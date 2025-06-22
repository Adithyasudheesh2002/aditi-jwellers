from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/shop')
def shop():
    return render_template('shop.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
