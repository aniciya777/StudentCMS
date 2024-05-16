import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Registration(SqlAlchemyBase):
    """
    ORM-модель регистрации на курс
    """

    __tablename__ = 'registrations'

    registration_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    student_id = sa.Column(sa.Integer, sa.ForeignKey('students.student_id'))
    course_id = sa.Column(sa.Integer, sa.ForeignKey('courses.course_id'))

    student = relationship('Student', backref='registrations')
    course = relationship('Course', backref='registrations')
    assessments = relationship('Assessment')

    def __repr__(self) -> str:
        return f'<Registration> {self.student} - {self.course}'

    def __str__(self) -> str:
        return f'{self.student} {self.course}'
