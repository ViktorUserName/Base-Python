from flask import render_template
from models.db import *


def show_disciplines():
    disciplines = get_all_disciplines()
    return render_template('index.html', disciplines=disciplines)

def show_disciple_students(disciple_id):
    disciple_students = get_disciple_students(disciple_id)
    return render_template('disciple_students.html', disciple_students=disciple_students)

def show_student_info(student_id):
    student_info = get_full_info(student_id)
    return render_template('info_students.html', student_info=student_info)

def create_grade(student_id, discipline_id, grade, date):
    grade_info = create_grade_for_student(student_id, discipline_id, grade, date)
    return grade_info
