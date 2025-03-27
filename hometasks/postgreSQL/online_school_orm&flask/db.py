from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func

# DB_CONFIG = {
#     'host': 'localhost',
#     'port': 5432,
#     'user': 'postgres',
#     'password': 'postgres',
#     'database': 'cinema',
# }

engine = create_engine("postgresql://postgres:postgres@localhost:5432/cinema", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

class Discipline(Base):
    __tablename__ = 'disciplies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))

    # Связи с ассоциативными таблицами
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

    __table_args__ = (
        CheckConstraint('grade BETWEEN 1 AND 10', name='grade_check'),
        CheckConstraint('date <= CURRENT_DATE', name='check_date_less_equal_today'),
    )

    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"))
    disciple_id = Column(Integer, ForeignKey('disciplies.id', ondelete="CASCADE"))

    student = relationship("Student", back_populates="grade_assocs")
    discipline = relationship("Discipline", back_populates="grade_assocs")






def get_db():
    pass