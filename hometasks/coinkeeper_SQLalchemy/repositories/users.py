from models.db_models import Session, Users

def update_balance(user_id, amount):
    with Session() as session:
        try:
            user = session.query(Users).filter(Users.id == user_id).first()
            if not user:
                return False
            user.balance += amount
            session.commit()
            return user.balance
        except Exception as e:
            print(e)
            session.rollback()
            return False