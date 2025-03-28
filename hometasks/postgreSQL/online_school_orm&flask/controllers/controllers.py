from flask import render_template
from models.db import *


def show_disciplines():
    disciplines = get_all_disciplines()
    return render_template('index.html', disciplines=disciplines)

def show_disciple_students(disciple_id):
    disciple_students = get_disciple_students(disciple_id)
    return render_template('disciple_students.html', disciple_students=disciple_students)
