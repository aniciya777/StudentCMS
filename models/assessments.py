import sqlalchemy as sa
import datetime

from .db_session import SqlAlchemyBase


class Assessment(SqlAlchemyBase):
    """
    ORM-модель оценки
    """

    __tablename__ = 'assessments'

    assessment_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    registration_id = sa.Column(sa.Integer, sa.ForeignKey('registrations.registration_id'))
    ball = sa.Column(sa.Integer, nullable=False, default=0)
    date = sa.Column(sa.Date, nullable=False, default=datetime.datetime.now)

    registration = sa.orm.relationship('Registration', back_populates='assessments')

    def __repr__(self) -> str:
        return f'<Assessment> {self.ball}'

    def __str__(self) -> str:
        return str(self.ball)
