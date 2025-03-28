from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, CheckConstraint, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func

engine = create_engine("postgresql://postgres:postgres@localhost:5432/courses", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
# session = Session()

class Discipline(Base):
    __tablename__ = "disciplies"
    # __table_args__ = {"schema": "courses"}  # Укажите вашу схему, если она не public

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))

    teacher_assocs = relationship("TeacherDisciple", back_populates="discipline")
    student_assocs = relationship("DiscipleStudent", back_populates="discipline")
    grade_assocs   = relationship("Grade", back_populates="discipline")


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    last_name = Column(String(30))

    disciple_assocs = relationship("DiscipleStudent", back_populates="student")
    grade_assocs    = relationship("Grade", back_populates="student")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(30))

    discipline_assocs = relationship("TeacherDisciple", back_populates="teacher")


class TeacherDisciple(Base):
    __tablename__ = 'teacher_disciple'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete="CASCADE"))
    disciple_id = Column(Integer, ForeignKey('disciplies.id', ondelete="CASCADE"))

    teacher = relationship("Teacher", back_populates="discipline_assocs")
    discipline = relationship("Discipline", back_populates="teacher_assocs")


class DiscipleStudent(Base):
    __tablename__ = 'disciple_student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    disciple_id = Column(Integer, ForeignKey('disciplies.id', ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"))

    discipline = relationship("Discipline", back_populates="student_assocs")
    student = relationship("Student", back_populates="disciple_assocs")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer)
    date = Column(Date, default=func.current_date(), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"))
    disciple_id = Column(Integer, ForeignKey('disciplies.id', ondelete="CASCADE"))

    __table_args__ = (
        CheckConstraint('grade BETWEEN 1 AND 10', name='grade_check'),
        CheckConstraint('date <= CURRENT_DATE', name='check_date_less_equal_today'),
    )
    student = relationship("Student", back_populates="grade_assocs")
    discipline = relationship("Discipline", back_populates="grade_assocs")


def init_db():
    Base.metadata.create_all(engine, checkfirst=True)

#                     ГЕТТЕРЫ
# ------------------------------------------------------------------
def get_all_disciplines():
    with Session() as session:
        return session.query(Discipline).all()

def get_all_students():
    with Session() as session:
        return session.query(Student).all()

def get_all_teachers():
    with Session() as session:
        return session.query(Teacher).all()

def get_all_grades_by_disciple(disciple_id):
    with Session() as session:
        result = session.query(Student.name, Discipline.title, Grade.grade, Grade.date) \
            .join(Grade, Grade.student_id == Student.id) \
            .join(Discipline, Grade.disciple_id == Discipline.id) \
            .filter(Discipline.id == disciple_id)
    return result

# SELECT disciplies.title, students.name, disciplies.id from disciple_student
# join disciplies on disciplies.id = disciple_student.disciple_id
# join students on students.id = disciple_student.student_id
# def get_disciple_students(disciple_id):
#     with Session() as session:
#         result = session.query(Discipline.title, Student.name, Discipline.id) \
#             .join(Discipline, DiscipleStudent.disciple_id == Discipline.id) \
#             .join(Student, DiscipleStudent.student_id == Student.id) \
#             .filter(Discipline.id == disciple_id)
#         return result

def get_disciple_students(disciple_id):
    with Session() as session:
        result = session.query(Discipline.title, Student.name, Student.id) \
            .join(DiscipleStudent, Discipline.id == DiscipleStudent.disciple_id) \
            .join(Student, Student.id == DiscipleStudent.student_id) \
            .filter(Discipline.id == disciple_id).all() # Выполнение запроса
        return result
result1 = get_disciple_students(1)
for student in result1:
    print(student)
# ------------------------------------------------------------------



# def all_teachers():
#     result = get_all_teachers()
#     for teacher in result:
#         print(teacher)