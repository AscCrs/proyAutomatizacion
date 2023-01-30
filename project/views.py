from flask import render_template, Blueprint, request, url_for
from project.data.models import Sensores_Template, Variables, Constantes, Calculos

content = Blueprint('content', __name__)

@content.route('/')
def home():
    return render_template('test.html')