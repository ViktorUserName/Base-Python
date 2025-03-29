from flask import Flask, render_template
from controllers import *
from controllers.controllers import show_disciplines, show_disciple_students, show_student_info

app = Flask(__name__)


@app.route('/')
def index():
    return show_disciplines()

@app.route('/disciplines/<int:disciple_id>')
def show_disciple_students_route(disciple_id):
    return show_disciple_students(disciple_id)

@app.route('/disciplines/student/<int:student_id>')
def show_info_student_route(student_id):
    return show_student_info(student_id)


if __name__ == '__main__':
    app.run(debug=True)

