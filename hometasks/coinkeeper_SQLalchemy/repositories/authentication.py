import bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.db_models import Users, Session
# import redis


# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def check_password(password, hashed_password):
    if not hashed_password:
        return False
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register_user(name, email, password):
    hashed_password = hash_password(password)
    new_user = Users(name=name, email=email, password=hashed_password)
    with Session() as session:
        try:
            session.add(new_user)
            session.commit()
            return new_user.id
        except Exception as e:
            session.rollback()
            print(f'Failed to register new user: {e}')
            return None


def login_user(email, password):
    with Session() as session:
        user = session.query(Users).filter_by(email=email).first()
        if not user:
            return None
        if check_password(password, user.password):
            access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

            # redis_client.setex(f"jwt:{user.id}", timedelta(days=1), access_token)

            return access_token
        return None
