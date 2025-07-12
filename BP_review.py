import os

from flask import Blueprint, redirect, render_template, url_for
from WTForms.reviewForm import ReviewForm
from db_models.db_session import *
from db_models.db_reviews import CrateReviews
from datetime import datetime
from sqlalchemy import and_

blueprint = Blueprint('review', __name__, template_folder='templates')
IMAGES_PATH = 'db/upload_images/'


@blueprint.route('/review', methods=['GET', "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():

        session = create_session()
        new_review = CrateReviews()
        print(form.grade.data)
        new_review.name = form.place_name.data
        new_review.address = form.address.data
        new_review.about = form.about.data
        new_review.grade = form.grade.data
        new_review.date = datetime.now().strftime('%Y-%m-%d-%H-%M')
        new_review.type_of_place = form.type_of_place.data
        file = form.photo
        os.makedirs(f'db/upload_images/{new_review.name} {new_review.address}', exist_ok=True)
        path = f"{new_review.name} {new_review.address}/{new_review.date}"
        file.data.save(IMAGES_PATH + path)
        new_review.image_filename = path
        print(new_review)
        session.add(new_review)
        session.commit()

        return redirect('/')
    if not form.validate_on_submit():
        print(form.errors)
    return render_template('review.html', form=form, title='review', file_css='css/review.css')
