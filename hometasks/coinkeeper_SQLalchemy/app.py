from flask import Flask, jsonify, request
from http import HTTPStatus
from flask_jwt_extended import JWTManager

from models.db_models import Session
from routes.privite import private_bp
from routes.public import public_bp
import models.db_models as db
import repositories.authentication as authentication



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

app.register_blueprint(private_bp)
app.register_blueprint(public_bp)



# ----------------------- Authentication
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), HTTPStatus.BAD_REQUEST

    user_id = authentication.register_user(data['name'], data['email'], data['password'])
    if user_id:
        return jsonify({'message': 'User registered'}), HTTPStatus.CREATED
    else:
        return jsonify({'message': 'User registration failed'}), HTTPStatus.BAD_REQUEST
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print(data)
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), HTTPStatus.UNAUTHORIZED

    access_token = authentication.login_user(data['email'], data['password'])
    if access_token:
        return jsonify({'access_token': access_token}), HTTPStatus.OK
    else:
        return jsonify({'message': 'Login failed'}), HTTPStatus.UNAUTHORIZED

# -------------------------------
def main():
    try:
        db.init_db()
        print('DB initialized successfully')
    except Exception as error:
        print(f'Error: {error}')

    try:
        app.run(port=5000, debug=True)
    except Exception as error:
        print(f'Error during server installization: {error}')

main()