from flask import Blueprint, render_template, redirect
from db_models.db_session import create_session
from db_models.db_places import Place
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, FileField, TextAreaField, SelectField

blueprint = Blueprint('all_places', __name__, template_folder='templates')

params = {
    "title": 'Все отзывы',
    "file_css": 'index.css',
    "types_of_place": ['Все', "Парк", "спортивный комплекс", "стадион", "ледовая арена", "развлекательный парк", "отель",
                       "ресторан", "кафе", "магазин", "рынок", "библиотека", "музей", "выставочный центр",
                       "образовательное учреждение", "медицинский центр", "пляж", "детская секция", "спортивная секция"]
}


class SomeForm(FlaskForm):
    select = SelectField("Тип места", choices=params['types_of_place'], coerce=str)
    submit = SubmitField('Обновить')


@blueprint.route('/all_places', methods=['GET', 'POST'])
def all_places():
    form = SomeForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.select.data)
        return redirect(f'/all_places?filter={form.select.data}')
    session = create_session()
    _filter = request.args.get('filter')
    if not _filter or _filter == 'Все':
        params['places'] = session.query(Place).all()
    else:
        params['places'] = session.query(Place).filter(Place.type_of_place == _filter).all()
    print(params["types_of_place"])
    return render_template("all_places.html", form=form, **params)
