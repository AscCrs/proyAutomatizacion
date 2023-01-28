from flask import render_template, Blueprint

content = Blueprint('content', __name__)

@content.route('/')
def home():
    return render_template('test.html')