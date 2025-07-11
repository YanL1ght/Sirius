from flask import Blueprint, redirect, render_template
from WTForms.reviewForm import ReviewForm
from db_models.db_session import *
from db_models.db_reviews import CrateReviews

blueprint = Blueprint('review', __name__, template_folder='templates')


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
        new_review.grade = int(form.grade.data)

        session.add(new_review)
        session.commit()

        return redirect('/')
    return render_template('review.html', form=form)
