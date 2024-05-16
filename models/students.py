import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Student(SqlAlchemyBase):
    """
    ORM-модель студента
    """

    __tablename__ = 'students'

    student_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.group_id'))

    group = relationship('Group', back_populates='students')
    courses = relationship('Course', secondary='registrations', viewonly=True)

    def __repr__(self) -> str:
        return f'<Student> {self.group} {self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
