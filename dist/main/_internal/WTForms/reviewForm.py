from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, FileField, TextAreaField, SelectField
from flask_wtf.file import FileRequired
from wtforms.validators import ValidationError

types_of_place = ['Парк', 'Спортивный комплекс', 'Стадион', 'Ледовая арена', 'Развлекательный парк', 'Отель',
                  'Ресторан', 'Кафе', 'Магазин', 'Рынок', 'Библиотека', 'Музей', 'Выставочный центр', "Торговый центр",
                  'Образовательное учреждение', 'Медицинский центр', 'Пляж', 'Детская секция', 'Спортивная секция']


def validate_photo(form, field):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    filename = field.data.filename.lower()
    if '.' not in filename or filename.rsplit('.', 1)[1] not in allowed_extensions:
        raise ValidationError('Разрешены только изображения с расширениями png, jpg, jpeg.')


class ReviewForm(FlaskForm):
    place_name = StringField('Place name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    about = TextAreaField('About', [validators.DataRequired()])
    photo = FileField('Image', validators=[FileRequired(), validate_photo])
    grade = SelectField('Ваша оценка',
                        choices=[(5, 'Отлично'), (4, "Хорошо"), (3, "Сойдёт"), (2, "Плохо"), (1, "Ужасно")],
                        coerce=int)
    type_of_place = SelectField("Тип места",
                                choices=types_of_place,
                                coerce=str)
    # recaptcha =
    submit = SubmitField('Отправить')


class SecondReviewForm(FlaskForm):
    about = TextAreaField('About', [validators.DataRequired()])
    grade = SelectField('Ваша оценка',
                        choices=[(5, 'Отлично'), (4, "Хорошо"), (3, "Сойдёт"), (2, "Плохо"), (1, "Ужасно")],
                        coerce=int)
    submit = SubmitField('Отправить')
