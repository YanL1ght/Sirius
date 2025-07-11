from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, FileField, TextAreaField, SelectField
from flask_wtf.file import FileAllowed, FileRequired


class ReviewForm(FlaskForm):
    place_name = StringField('Place name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    about = TextAreaField('About', [validators.DataRequired()])
    # photo = FileField('Image', validators=[FileRequired(), FileAllowed(["jpg", "png"])])
    grade = SelectField('Ваша оценка', choices=[5, 4, 3, 2, 1], coerce=int)
    # recaptcha =
    submit = SubmitField('Send')
