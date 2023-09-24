from models import Student, Subject, StudentSubject
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random

db_uri = 'postgresql://postgres:533653@localhost:5432/students_bd'
engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

names = ["Дмитро", "Олена", "Іван", "Марія", "Андрій", "Наталія",
         "Сергій", "Анна", "Петро", "Юлія"]
for _ in range(10):
    student = Student(
        name=random.choice(names),
        age=random.randint(18, 25)
    )
    session.add(student)

subjects = ["Математика", "Фізика", "Хімія", "Література",
            "Історія", "Англійська", "Географія", "Інформатика"]
for subject_name in subjects:
    subject = Subject(name=subject_name)
    session.add(subject)

students = session.query(Student).all()
for student in students:
    for _ in range(random.randint(1, len(subjects))):
        student_subject = StudentSubject(
            student=student,
            subject_id=random.randint(1, len(subjects)),
            grade=random.randint(1, 5)
        )
        session.add(student_subject)

session.commit()
session.close()
