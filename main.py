import os
from pprint import pprint

from models.db_session import global_init, create_session
from models import *

DB_NAME = 'db/crm.sqlite'


if __name__ == '__main__':
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    global_init(DB_NAME)
    db_sess = create_session()
    db_sess.add(my_group := Group(title='ПМИ-201', year_ed=4))
    db_sess.add(Group(title='ПМИ-231', year_ed=1))

    db_sess.add(my := Student(first_name='Анастасия', last_name='Остапчук', group=my_group))
    db_sess.add(Student(first_name='Олусо', last_name='Гуапова', group=my_group))
    #
    db_sess.add(my_teacher := Teacher(first_name='Алексей', last_name='Клячин', job_title='Заведующий кафедрой'))
    db_sess.add(Teacher(first_name='Александр', last_name='Иванов', job_title='Ассистент'))

    db_sess.add(exam := TypeOfCertification(title='Экзамен'))
    db_sess.add(diff_zach := TypeOfCertification(title='Дифференцированный зачет'))
    db_sess.add(TypeOfCertification(title='Зачет'))

    db_sess.add(my_subject := Course(title='Системы и методы компьютерного моделирования', teacher=my_teacher, type_of_certification=diff_zach))
    db_sess.add(Course(title='Математический анализ', teacher=my_teacher, type_of_certification=exam))

    db_sess.add(current_course := my_subject.register(my))

    current_course.assessments.append(Assessment(ball=25))
    current_course.assessments.append(Assessment(ball=25))
    current_course.assessments.append(Assessment(ball=25))
    current_course.assessments.append(Assessment(ball=25))

    db_sess.commit()

    for title, table in (
            ('ГРУППЫ', Group),
            ('ПРЕПОДАВАТЕЛИ', Teacher),
            ('СТУДЕНТЫ', Student),
            ('КУРСЫ', Course),
            ('ТИПЫ СЕРТИФИКАЦИИ', TypeOfCertification),
            ('РЕГИСТРАЦИИ', Registration),
            ('ОЦЕНКИ', Assessment)
    ):
        print('#' * 80)
        print(f'ВСЕ {title}')
        pprint(db_sess.query(table).all())
        print()
