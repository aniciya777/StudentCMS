import sqlalchemy as sa

from .db_session import SqlAlchemyBase


class TypeOfCertification(SqlAlchemyBase):
    """
    ORM-модель типа аттестации
    """

    __tablename__ = 'type_of_certification'

    type_of_certification_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'<TypeOfCertification> {self.title}'

    def __str__(self) -> str:
        return self.title
