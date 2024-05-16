import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    """
    ORM-модель группы студентов
    """

    __tablename__ = 'groups'

    group_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True)
    year_ed = sa.Column(sa.Integer, nullable=True, default=1)

    students = relationship('Student')

    def __repr__(self) -> str:
        return f'<Group> {self.title} {self.year_ed}'

    def __str__(self) -> str:
        return self.title
