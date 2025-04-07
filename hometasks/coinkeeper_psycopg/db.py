import psycopg2
# import bcrypt
# from flask_jwt_extended import create_access_token

DB_CONFIG = {
    "dbname": "coinkeeper",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS users
        (               
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            main_balance DECIMAL(15, 2) NOT NULL DEFAULT 0,
        
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

        cur.execute("""CREATE TABLE IF NOT EXISTS categories
            (   
            id SERIAL PRIMARY KEY,
            title VARCHAR(30),
        
            user_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );  
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS transactions
            (
                id SERIAL PRIMARY KEY,
                transaction_type TEXT CHECK (type IN ('income', 'expense')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                category_id INT NOT NULL,
                user_id INT NOT NULL,
                amount INT NOT NULL,

            
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)

        conn.commit()


def get_all_category():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT c.title, u.username FROM categories c join users u on u.id = c.user_id")

        categories = cur.fetchall()
        return categories

def get_category_by_id(category_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT c.title, u.username FROM categories c join users u on u.id = c.user_id WHERE c.id = %s", (category_id,))

        category_from_db = cur.fetchone()
        category = {
            'title': category_from_db[0],
            'username': category_from_db[1],
        }
        return category

def create_transaction(transaction_type, category_id, user_id, amount):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""INSERT INTO transactions (transaction_type, category_id, user_id, amount) VALUES (%s, %s, %s, %s) RETURNING id""",
                    (transaction_type, category_id, user_id, amount))

        transaction_id = cur.fetchone()[0]

        if transaction_type == 'income':
            cur.execute("""
                           UPDATE users
                           SET main_balance = main_balance + %s
                           WHERE id = %s
                           RETURNING main_balance;
                       """, (amount, user_id))
        elif transaction_type == 'expense':
            cur.execute("""
                           UPDATE users
                           SET main_balance = main_balance - %s
                           WHERE id = %s
                           RETURNING main_balance;
                       """, (amount, user_id))

        new_balance = cur.fetchone()[0]

        conn.commit()
        return transaction_id


def search_categories(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM coinb WHERE title ILIKE %s;", (f"%{query}%",))

        categories = cur.fetchall()
        return categories