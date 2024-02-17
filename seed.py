from conf.models import session, Student, Group, Subject, Teacher, Grades
from faker import Faker
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from conf.db import URI
from random import randint

fake = Faker('uk_UA')
engine = create_engine(URI)

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

name_group = ['GroupA', 'GroupB', 'GroupC']
subject_name = ['Математика', 'Физика', 'Біологія']


def gen_data(session):
    try:
        # Prepare data
        students = []
        groups = []
        teachers = []
        subjects = []
        grades = []

        # Create groups
        for i in range(1, 4):
            group = Group(id=i, name=name_group[i - 1])
            groups.append(group)
            print('Group')

        # Create teachers
        for i in range(1, 4):
            teacher_name = fake.name()
            teacher = Teacher(id=i, name=teacher_name)
            teachers.append(teacher)
            print('Teacher')

        # Create subjects
        for i in range(1, 4):
            subject = Subject(id=i, name=subject_name[i - 1], teacher_id=randint(1, 3))
            subjects.append(subject)
            print('Subject')

        # Add prepared data to the database
        session.add_all(groups)
        session.add_all(teachers)
        session.add_all(subjects)
        session.commit()

        # Create students
        for id in range(1, 31):
            student_name = fake.name()
            student = Student(id=id, name=student_name, group_id=fake.random_int(min=1, max=3),
                              teacher_id=fake.random_int(min=1, max=3))
            students.append(student)
            print('student')

        session.add_all(students)
        session.commit()

        # Create grades
        for student in students:
            for subject in subjects:
                grades_value = randint(2, 5)  # Генерируем случайную оценку от 2 до 5
                date_received = fake.date_between(start_date='-1y', end_date='today')
                grade = Grades(student_id=student.id, subject_id=subject.id, grade=grades_value, date=date_received)
                grades.append(grade)
                print('Grades')

        session.add_all(grades)
        session.commit()

        print('OK')
    except Exception as err:
        print(err)
        print('NO')


top_students = (
    session.query(Grades.student_id, func.avg(Grades.grade).label('average_grade'))
    .group_by(Grades.student_id)
    .order_by(func.avg(Grades.grade).desc())
    .limit(5)
    .all()
)

# Вывод результатов

courses = session.query(Subject).join(Teacher).filter(Teacher.id == 3).all()
student = session.query(Student).join(Group).filter(Group.id == 1).all()

courses = session.query(Subject).join(Grades).join(Teacher).filter(Teacher.id == 2).filter(
    Grades.student_id == 2).filter(Subject.id == 2).all()

name_student = session.query(func.avg(Grades.grade)).join(Student).join(Group).join(Subject).filter(Subject.id == 2)
