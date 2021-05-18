from flask import Blueprint, render_template

# consolidates routes onto a single bp object ==> Router middleware
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  # renders template instead of string
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

# <id> parameter for single(id) function
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')