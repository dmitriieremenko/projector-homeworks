from sqlalchemy import create_engine, text

db_uri = 'postgresql://postgres:533653@localhost:5432/students_bd'
engine = create_engine(db_uri)


sql_query = text("""
    SELECT students.name
    FROM students
    JOIN student_subjects ON students.id = student_subjects.student_id
    JOIN subjects ON student_subjects.subject_id = subjects.id
    WHERE subjects.name = :subject_name
""")


with engine.connect() as connection:
    query_parameters = {"subject_name": "Англійська"}
    english_students_result = connection.execute(sql_query, query_parameters)
    english_students = english_students_result.fetchall()


for student_name in english_students:
    print(student_name[0])
