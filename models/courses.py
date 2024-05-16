import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase
from .students import Student
from .registrations import Registration


class Course(SqlAlchemyBase):
    """
    ORM-модель курса
    """

    __tablename__ = 'courses'

    course_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    type_of_certification_id = sa.Column(sa.Integer, sa.ForeignKey('type_of_certification.type_of_certification_id'))
    teacher_id = sa.Column(sa.Integer, sa.ForeignKey('teachers.teacher_id'))
    title = sa.Column(sa.String, nullable=False, unique=True)

    students = relationship('Student', secondary='registrations', back_populates='courses', viewonly=True)
    type_of_certification = relationship('TypeOfCertification')
    teacher = relationship('Teacher', back_populates='courses')

    def register(self, student: Student) -> Registration:
        return Registration(course=self, student=student)

    def __repr__(self) -> str:
        return f'<Course> {self.title}'

    def __str__(self) -> str:
        return self.title
