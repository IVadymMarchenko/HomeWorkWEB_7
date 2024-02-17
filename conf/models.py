from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func, DateTime, DATE, \
    Column
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///:memory:', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship('Teacher', back_populates='students')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    students = relationship('Student', back_populates='teacher')


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship('Teacher')


class Grades(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject_id = Column(Integer, ForeignKey('subject.id', ondelete='CASCADE', onupdate='CASCADE'))
    grade = Column(Integer)
    date = Column(DateTime)


Base.metadata.create_all(engine)
