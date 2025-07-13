from flask import Blueprint, render_template, redirect
from db_models.db_session import create_session
from db_models.db_places import Place
from flask import request
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

blueprint = Blueprint('all_places', __name__, template_folder='templates')

params = {
    "title": 'Все отзывы',
    "file_css": 'index.css',
    "types_of_place": ['Все', 'Парк', 'Спортивный комплекс', 'Стадион', 'Ледовая арена', 'Развлекательный парк',
                       "Торговый центр",
                       'Отель', 'Ресторан', 'Кафе', 'Магазин', 'Рынок', 'Библиотека', 'Музей', 'Выставочный центр',
                       'Образовательное учреждение', 'Медицинский центр', 'Пляж', 'Детская секция', 'Спортивная секция']
}


class SomeForm(FlaskForm):
    select = SelectField("Тип места", choices=params['types_of_place'], coerce=str)
    submit = SubmitField('Обновить')


@blueprint.route('/all_places', methods=['GET', 'POST'])
def all_places():
    form = SomeForm()
    if form.validate_on_submit():
        return redirect(f'/all_places?filter={form.select.data}')
    session = create_session()
    _filter = request.args.get('filter')
    if not _filter or _filter == 'Все':
        params['places'] = session.query(Place).all()
    else:
        params['places'] = session.query(Place).filter(Place.type_of_place == _filter).all()
    return render_template("all_places.html", form=form, **params)
