import sqlalchemy as sa
from db_models import db_session
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Place(db_session.SqlAlchemyBase):
    __tablename__ = 'places'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    address = sa.Column(sa.String, nullable=False)
    about = sa.Column(sa.String)
    image_filename = sa.Column(sa.String, default='static/images/filler.jpg')
    type_of_place = sa.Column(sa.String, nullable=False)
    grade = sa.Column(sa.Float, nullable=False)
    reviews = relationship('CrateReviews', back_populates='place')
