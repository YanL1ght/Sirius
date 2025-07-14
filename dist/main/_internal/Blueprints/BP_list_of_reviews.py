from flask import Blueprint, render_template, send_from_directory
from db_models.db_session import create_session
from db_models.db_places import Place
from db_models.db_reviews import CrateReviews

blueprint = Blueprint('list_of_reviews', __name__, template_folder='templates')

params = {
    "title": 'Все отзывы',
    "file_css": 'list_of_reviews.css',
    'places_params': {},
    'dates': [],
}


@blueprint.route('/list_of_reviews')
def list_of_reviews():
    session = create_session()
    params['reviews'] = session.query(CrateReviews).all()

    for place in session.query(Place).all():
        params['places_params'][place.id] = {
            "name": place.name,
            'address': place.address
        }

    for i in params['reviews']:
        date = i.date.split('-')
        final = '.'.join(date[:3]) + ' в ' + ':'.join(date[3:])
        params["dates"].append(final)

    return render_template("list_of_reviews.html", **params)
