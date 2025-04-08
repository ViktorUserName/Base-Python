from sqlalchemy.exc import NoResultFound

from models.db_models import Categories, Session, Users


def get_all_categories():
    with Session() as session:
        try:
            categories = session.query(Categories.id, Categories.title, Users.name.label('user_name')) \
                .join(Users).all()
            if categories is not None:
                categories_list = [{'id': category.id, 'title': category.title, 'user_name' : category.user_name} for category in categories]
                return categories_list
            else:
                return None
        except Exception as e:
            print(f'Error: {e}')
            return None

def create_category(title, user_id):
    with Session() as session:
        try:
            category = Categories(title=title, user_id=user_id)
            session.add(category)
            session.commit()
            return {'id': category.id, 'title': category.title, 'user_id': category.user_id}
        except Exception as e:
            session.rollback()
            print(f'Error: {e}')
            return {'error': 'Failed to create category'}