from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, CheckConstraint, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func

engine = create_engine("postgresql://postgres:postgres@localhost:5432/courses", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
# session = Session()

class Discipline(Base):
    __tablename__ = "disciplies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))

    teacher_assocs = relationship("TeacherDisciple", back_populates="discipline")
    student_assocs = relationship("DiscipleStudent", back_populates="discipline")
    grade   = relationship("Grade", back_populates="discipline")
    student = relationship("Student",secondary='disciple_student', back_populates="discipline")


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    last_name = Column(String(30))

    disciple_assocs = relationship("DiscipleStudent", back_populates="student")
    grade_assocs    = relationship("Grade", back_populates="student")
    discipline = relationship('Discipline', secondary='disciple_student', back_populates="student")


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
    discipline = relationship("Discipline", back_populates="grade")


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

# def get_disciple_students(disciple_id):
#     with Session() as session:
#         result = session.query(Discipline.title, Student.name, Student.id) \
#             .join(DiscipleStudent, Discipline.id == DiscipleStudent.disciple_id) \
#             .join(Student, Student.id == DiscipleStudent.student_id) \
#             .filter(Discipline.id == disciple_id).all() # Выполнение запроса
#         return result

def get_disciple_students(disciple_id):
    with Session() as session:
        discipline = session.query(Discipline).filter(Discipline.id == disciple_id).first()
        if not discipline:
            return None
        return {
            'id': discipline.id,
            'Disciple': discipline.title,
            'Student': {s.name : s.id for s in discipline.student},
        }
print(get_disciple_students(1))

# ------------------------------------------------------------------
def get_full_info(student_id):
    with Session() as session:
        student = session.query(Student).filter(Student.id == student_id).first()
        if not student:
            return None
        return {
            'id': student.id,
            'name': student.name,
            'last_name': student.last_name,
            'disciple':
                {d.title: [g.grade for g in d.grade if g.student_id == student.id]
                for d in student.discipline},
            'grades':[g.grade for g in student.grade_assocs],
        }

# def get_grades_by_disciple(disciple_id):
#     with Session() as session:
#         discipline = session.query(Discipline).filter(Discipline.id == disciple_id).first()
#         return {
#             'disciple': discipline.title,
#             'grades':[g.grade for g in discipline.grade],
#         }

# print(get_grades_by_disciple(1))
# print(get_full_info(1))