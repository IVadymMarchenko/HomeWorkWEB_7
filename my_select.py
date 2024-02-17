from seed import session
from sqlalchemy import func
from conf.models import Student, Group, Subject, Teacher, Grades


def select_1(session):
    top_students = (
        session.query(Grades.student_id, func.avg(Grades.grade).label('average_grade'))
        .group_by(Grades.student_id)
        .order_by(func.avg(Grades.grade).desc())
        .limit(5)
        .all()
    )
    for i in top_students:
        print(f'student id : {i.student_id}, grades: {i.average_grade}')


def select_2(session):
    max_grade = session.query(Student, func.avg(Grades.grade).label('average_grade')) \
        .join(Grades).join(Subject).filter(Subject.id == 1) \
        .group_by(Student.id) \
        .order_by(func.avg(Grades.grade).desc()) \
        .first()
    student, average_grade = max_grade
    print(student.name, student.id)


def select_3(session):
    name_student = session.query(func.avg(Grades.grade)).join(Student).join(Group).join(Subject).filter(Subject.id == 2)
    subject = session.query(Subject).filter(Subject.id == 2).first()
    for i in name_student:
        print(subject.name, round(i[0], 3))


def select_4(session):
    student = session.query(func.avg(Grades.grade)).scalar()
    print(student)


def select_5(session):
    print('Знайти які курси читає певний викладач.')
    courses = session.query(Subject).join(Teacher).filter(Teacher.id == 3).all()
    for i in courses:
        print(i.name, f'id teacher is 3')


def select_6(session):
    print('Знайти список студентів у певній групі.')
    student = session.query(Student).join(Group).filter(Group.id == 1).all()
    for i in student:
        print(i.name)


def select_7(session):
    print('Знайти оцінки студентів у окремій групі з певного предмета.')
    subject_name = "Біологія"  # Назва предмета
    group_name = "GroupA"  # Назва групи

    # Здійснюємо з'єднання таблиць за допомогою методу join() та використовуємо фільтри
    grades = session.query(Grades). \
        join(Student). \
        join(Group). \
        join(Subject). \
        filter(Group.name == group_name). \
        filter(Subject.name == subject_name). \
        all()

    # Виведення результатів
    if grades:
        for grade in grades:
            print("Студент:", grade.student_id, "| Оцінка:", grade.grade)
    else:
        print("Дані відсутні")


def select_8(session):
    print('Знайти середній бал, який ставить певний викладач зі своїх предметів.')
    ball = session.query(func.avg(Grades.grade)).join(Subject).filter(Subject.teacher_id == 2).scalar()
    print(ball)


def select_9(session):
    print('Знайти список курсів, які відвідує певний студент.')
    courses = session.query(Subject).join(Grades).filter(Grades.student_id == 1).all()
    for i in courses:
        print(i.name)


def select_10(session):
    print('Список курсів, які певному студенту читає певний викладач.')
    courses = session.query(Subject).join(Grades).join(Teacher).filter(Teacher.id == 2).filter(
        Grades.student_id == 2).filter(Subject.id == 2).all()
    for i in courses:
        print(i.name)

# select_1(session)
# select_2(session)
# select_3(session)
# select_4(session)
# select_5(session)
# select_6(session)
# select_7(session)
# select_8(session)
# select_9(session)
# select_10(session)
