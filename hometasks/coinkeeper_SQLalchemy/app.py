from flask import Flask, jsonify, request
from http import HTTPStatus
from flask_jwt_extended import JWTManager
import models.db_models as db

# from routes.public import public_bp
# from routes.privite import private_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)


# -------------------------------
def main():
    try:
        # db.init_db()
        print('DB initialized successfully')
    except Exception as error:
        print(f'Error: {error}')

    try:
        app.run(port=5000, debug=True)
    except Exception as error:
        print(f'Error during server installization: {error}')

main()