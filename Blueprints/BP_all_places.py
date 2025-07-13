from flask import Blueprint, render_template, send_from_directory
from db_models.db_session import create_session
from db_models.db_places import Place

blueprint = Blueprint('all_places', __name__, template_folder='templates')

params = {
    "title": 'Все отзывы',
    "file_css": 'index.css'
}


@blueprint.route('/all_places')
def all_places():
    session = create_session()
    params['places'] = session.query(Place).all()

    return render_template("all_places.html", **params)
