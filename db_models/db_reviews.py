import sqlalchemy as sa
from db_models import db_session


class CrateReviews(db_session.SqlAlchemyBase):
    __tablename__ = 'review'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    address = sa.Column(sa.String, nullable=False)
    about = sa.Column(sa.String, nullable=False)
    image_filename = sa.Column(sa.String, default='static/images/filler.jpg')
    grade = sa.Column(sa.Integer, nullable=False)
    type_of_place = sa.Column(sa.String, nullable=False)
    date = sa.Column(sa.String, nullable=False)


