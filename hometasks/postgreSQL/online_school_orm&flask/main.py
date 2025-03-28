from flask import Flask, render_template
from controllers import *
from controllers.controllers import show_disciplines, show_disciple_students

app = Flask(__name__)


@app.route('/')
def index():
    return show_disciplines()

@app.route('/disciplines/<int:disciple_id>')
def show_disciple_students_route(disciple_id):
    return show_disciple_students(disciple_id)


if __name__ == '__main__':
    app.run(debug=True)

