from flask import Blueprint, render_template, send_from_directory
from db_models.db_session import create_session
from db_models.db_places import Place

blueprint_home = Blueprint('home', __name__, template_folder='templates')

params = {
    "title": 'Добро пожаловать!',
    "file_css": 'index.css',
    'places': []
}


@blueprint_home.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('db/upload_images', filename)


@blueprint_home.route('/')
def index():
    session = create_session()
    params['places'] = session.query(Place).all()[:6]
    return render_template("index.html", **params)
