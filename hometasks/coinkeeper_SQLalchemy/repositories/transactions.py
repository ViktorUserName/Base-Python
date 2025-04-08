from models.db_models import Session, Transactions, Users

def create_transaction(user_id, category_id, transaction_type, amount):
    with Session() as session:
        try:
            transaction = Transactions(
                user_id = user_id,
                category_id = category_id,
                transaction_type = transaction_type,
                amount = amount
            )
            user_balance = session.query(Users).filter(Users.id == user_id).first()
            if transaction.transaction_type == 'income':
                user_balance.balance += amount
            elif transaction.transaction_type == 'expense':
                user_balance.balance -= amount
            session.add(transaction)
            session.commit()
            return {'id': transaction.id, 'user_id': transaction.user_id, 'category_id': transaction.category_id, 'transaction_type': transaction.transaction_type, 'amount': transaction.amount, 'balance': user_balance.balance}
        except Exception as e:
            session.rollback()
            print(f'failed to create transaction: {e}')
            return {'error': 'Failed to create transaction'}