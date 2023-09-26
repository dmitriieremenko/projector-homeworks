from models import Student, Subject, StudentSubject
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import aliased

db_uri = 'postgresql://postgres:533653@localhost:5432/students_bd'
engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

students_alias = aliased(Student)
student_subjects_alias = aliased(StudentSubject)

english_students = (
    session.query(students_alias.name)
    .join(student_subjects_alias,
          students_alias.id == student_subjects_alias.student_id)
    .join(Subject, student_subjects_alias.subject_id == Subject.id)
    .filter(Subject.name == "Англійська")
    .all()
)

for student_name in english_students:
    print(student_name[0])
