from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db_uri = 'postgresql://postgres:533653@localhost:5432/students_bd'
engine = create_engine(db_uri)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class StudentSubject(Base):
    __tablename__ = 'student_subjects'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    grade = Column(Integer, nullable=False)

    student = relationship('Student', backref='student_subjects')
    subject = relationship('Subject', backref='student_subjects')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
