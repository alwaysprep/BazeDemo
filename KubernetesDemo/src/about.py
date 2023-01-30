from flask import Blueprint


about = Blueprint('about', __name__)

@about.route('/')
def hello_world():
    return "<p>About page2</p>"

