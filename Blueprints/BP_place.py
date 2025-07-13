from flask import Blueprint, render_template, send_from_directory
from db_models.db_session import create_session
from db_models.db_places import Place
from db_models.db_reviews import CrateReviews
from WTForms.reviewForm import SecondReviewForm
from datetime import datetime

blueprint = Blueprint('place', __name__, template_folder='templates')

params = {
    "file_css": 'place.css',
    "dates": []
}



@blueprint.route('/place/<int:place_id>', methods=['GET', "POST"])
def place_page(place_id):
    session = create_session()
    place = session.query(Place).filter(Place.id == place_id).first()
    if not place:
        return 'такого местечка у нас не найдётся'
    form = SecondReviewForm()
    if form.validate_on_submit():
        new_review = CrateReviews()
        new_review.place_id = place.id
        new_review.about = form.about.data
        new_review.grade = form.grade.data
        new_review.date = datetime.now().strftime('%Y-%m-%d-%H-%M')

        place_ = session.query(Place).filter(Place.id == new_review.place_id).first()
        grades = session.query(CrateReviews).filter(CrateReviews.place_id == new_review.place_id).all()
        _len = len(grades) + 1
        _sum = sum(list(map(lambda x: x.grade, grades))) + new_review.grade  # сумма всех оценок
        setattr(place_, "grade", round(_sum / _len, 1))
        session.add(new_review)
        session.commit()
        return render_template('alert.html')

    params['place'] = place
    params['title'] = place.name
    params['reviews'] = session.query(CrateReviews).filter(CrateReviews.place_id == place_id).all()
    params["form"] = form

    for i in params['reviews']:
        date = i.date.split('-')
        final = '.'.join(date[:3]) + ' в ' + ':'.join(date[3:])
        params["dates"].append(final)
    return render_template("place.html", **params)
