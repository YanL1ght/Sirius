import sqlalchemy as sa
from db_models import db_session
from sqlalchemy.orm import relationship


class CrateReviews(db_session.SqlAlchemyBase):
    __tablename__ = 'review'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    place_id = sa.Column(sa.Integer, sa.ForeignKey('places.id'), nullable=False)
    about = sa.Column(sa.String)
    grade = sa.Column(sa.Integer, nullable=False)
    date = sa.Column(sa.String, nullable=False)
    place = relationship('Place', back_populates='reviews')

