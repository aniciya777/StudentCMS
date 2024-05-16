import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Teacher(SqlAlchemyBase):
    """
    ORM-модель преподавателя
    """

    __tablename__ = 'teachers'

    teacher_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    job_title = sa.Column(sa.String, nullable=True)

    courses = relationship('Course')

    def __repr__(self) -> str:
        return f'<Teacher> {self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
