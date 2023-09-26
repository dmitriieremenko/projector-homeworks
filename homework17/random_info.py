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
subjects = ["Математика", "Фізика", "Хімія", "Література",
            "Історія", "Англійська", "Географія", "Інформатика"]

for subject_name in subjects:
    subject = Subject(name=subject_name)
    session.add(subject)
session.commit()

for _ in range(10):
    student = Student(
        name=random.choice(names),
        age=random.randint(18, 25)
    )
    session.add(student)
session.commit()

students = session.query(Student).all()
for student in students:
    num_subjects = random.randint(1, len(subjects))
    subject_indices = random.sample(range(len(subjects)), num_subjects)
    for idx in subject_indices:
        existing_record = session.query(StudentSubject).filter_by(
            student_id=student.id, subject_id=idx + 1).first()
    if not existing_record:
        student_subject = StudentSubject(
            student=student,
            subject_id=idx + 1,
            grade=random.randint(1, 5)
        )
        session.add(student_subject)
session.commit()
session.close()
