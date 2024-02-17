from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship


engine = create_engine('sqlite:///:memory:', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Students(Base):
    __tablename__='students'

    id: Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    group_id:Mapped[int]=mapped_column(ForeignKey('groups.id'))


class Group(Base):
    __tablename__='groups'

    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[int]=mapped_column(String(50))


class Teachers(Base):
    __tablename__='teacher'

    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str]=mapped_column(String(50))

class Subject(Base):
    __tablename__='subject'
    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str]=mapped_column(String(50))
    teacher_id:Mapped[int]=mapped_column(autoincrement='teacher.id')


class Grades(Base):
    __tablename__='grades'

    id: Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    student_id: Mapped[int]=mapped_column(Integer,ForeignKey('students.id'))
    subject_id: Mapped[int]=mapped_column(Integer,ForeignKey('subject.id'))
    grade:Mapped[int]=mapped_column(Integer)
    date:Mapped[DateTime]=mapped_column(DateTime)


Base.metadata.create_all(engine)





