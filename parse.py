import argparse
from seed import session
from conf.models import Student, Group, Subject, Teacher, Grades


def create_teacher(session, name):
    try:
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
        print(f'Створено вчителя з ім\'ям "{name}"')
    except Exception as err:
        print(err)
        print('NO')


def list_teachers(session):
    techers = session.query(Teacher).all()
    for techer in techers:
        print(techer.name)


def update_teacher(session, id, name):
    new_teacher = session.query(Teacher).filter(Teacher.id == id).first()
    if new_teacher:
        try:
            new_teacher.name = name
            session.commit()
            print('OK')
            print(f'Оновлено дані вчителя з id={id}, нове ім\'я: "{name}"')
        except Exception as err:
            print(err)
            print('NO')


def remove_teacher(session, id):
    teacher = session.query(Teacher).filter(Teacher.id == id).first()
    if teacher:
        try:
            session.delete(teacher)
            session.commit()
            print(f'Видалено вчителя з id={id}')
        except Exception as err:
            print(err)


def main():
    parser = argparse.ArgumentParser(description="CLI програма для взаємодії з базою даних")

    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"],
                        help="Операція (create, list, update, remove)", required=True)
    parser.add_argument("-m", "--model", choices=["Teacher", "Group", "Subject", "Grades"],
                        help="Модель для виконання операції", required=True)
    parser.add_argument("-i", "--id", type=int, help="ID запису")
    parser.add_argument("-n", "--name", help="Ім'я запису")

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Teacher":
            create_teacher(session, args.name)
        # Додати інші моделі
    elif args.action == "list":
        if args.model == "Teacher":
            list_teachers(session)
        # Додати інші моделі
    elif args.action == "update":
        if args.model == "Teacher":
            update_teacher(session, args.id, args.name)
        # Додати інші моделі
    elif args.action == "remove":
        if args.model == "Teacher":
            remove_teacher(session, args.id)
        # Додати інші моделі


if __name__ == "__main__":
    main()