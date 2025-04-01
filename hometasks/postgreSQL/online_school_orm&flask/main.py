from flask import Flask, render_template, request, redirect, url_for, jsonify
from controllers import *
from controllers.controllers import show_disciplines, show_disciple_students, show_student_info, create_grade

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

@app.route('/create_grade', methods=['POST'])
def create_grade_route():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    student_id = data.get('student_id')
    discipline_id = data.get('discipline_id')
    grade = data.get('grade')
    date = data.get('date')

    if not all([student_id, discipline_id, grade, date]):
        return jsonify({'error': 'No data provided'}), 400

    result = create_grade(student_id, discipline_id, grade, date)

    return jsonify({"message": "grade created", "data": result})

# @app.route('/create_grade', methods=['POST'])
# def create_grade_route():
#     student_id = request.form.get('student_id')
#     discipline_id = request.form.get('discipline_id')
#     grade = request.form.get('grade')
#     date = request.form.get('date')
#
#     create_grade(student_id, discipline_id, grade, date)
#
#     return redirect(url_for('show_disciple_students_route', discipline_id=discipline_id))

if __name__ == '__main__':
    app.run(debug=True)