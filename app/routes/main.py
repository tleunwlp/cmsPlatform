from flask import Blueprint, render_template
from app.models import generate_gpt_question

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/generate_question/<category>', methods=['GET'])
def generate_question(category):
    question = generate_gpt_question(category)
    return f"질문 : {question}"