from flask import Blueprint, render_template
from WTForms.reviewForm import ReviewForm
from db_models.db_session import *
from db_models.db_reviews import CrateReviews
from db_models.db_places import Place
from datetime import datetime


blueprint_review = Blueprint('review', __name__, template_folder='templates')
IMAGES_PATH = 'db/upload_images/'


@blueprint_review.route('/review', methods=['GET', "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        session = create_session()
        place = session.query(Place).filter(
            Place.name == form.place_name.data,
            Place.address == form.address.data).first()
        new_review = CrateReviews()
        file = form.photo.data
        extension = file.filename[file.filename.index('.'):]
        path = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + extension}"
        if not place:
            new_place = Place()
            new_place.name = form.place_name.data
            new_place.address = form.address.data
            new_place.about = form.about.data
            new_place.type_of_place = form.type_of_place.data
            new_place.image_filename = path
            new_place.grade = float(form.grade.data)
            session.add(new_place)
            session.flush()

            file.save(IMAGES_PATH + path)

            new_review.place_id = session.query(Place).filter(
            Place.name == new_place.name,
            Place.address == new_place.address).first().id
            new_review.grade = form.grade.data
            new_review.about = form.about.data
        else:
            new_review.grade = form.grade.data
            new_review.date = datetime.now().strftime('%Y-%m-%d-%H-%M')
            new_review.type_of_place = form.type_of_place.data
            new_review.place_id = place.id

            place_ = session.query(Place).filter(Place.id == new_review.place_id).first()
            grades = session.query(CrateReviews).filter(CrateReviews.place_id == new_review.place_id).all()
            _len = len(grades) + 1
            _sum = sum(list(map(lambda x: x.grade, grades))) + new_review.grade  # сумма всех оценок
            setattr(place_, "grade", round(_sum / _len, 1))

        new_review.about = form.about.data
        new_review.date = datetime.now().strftime('%Y-%m-%d-%H-%M')
        session.add(new_review)
        session.commit()

        return render_template('alert.html')
    return render_template('review.html', form=form, title='review', file_css='review.css')
