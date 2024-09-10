from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('Profile.html')

@main.route('/robots.txt')
def robots():
    
    return render_template('robots.html')

@main.route('/smith')
def smith():
    return render_template('smith.html')
