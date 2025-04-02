import psycopg2
import bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

DB_CONFIG = {
    "dbname": "to_do_list",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(30),
                email VARCHAR(30) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                status TEXT CHECK (status IN ('new', 'in progress', 'done')) DEFAULT 'new' NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT NULL,
                deleted_at TIMESTAMP DEFAULT NULL,

                user_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS subtasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                status TEXT CHECK (status IN ('done', 'not done')) DEFAULT 'not done' NOT NULL,

                task_id INT NOT NULL,
                FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id SERIAL PRIMARY KEY,
                name VARCHAR(30) UNIQUE NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS task_tags (
                id SERIAL PRIMARY KEY,
                task_id INT NOT NULL,
                tag_id INT NOT NULL,
                FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
            );
        """)
        conn.commit()


def get_all_tasks():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT tasks.id,
               tasks.title,
               tasks.description,
               tasks.status,
               tasks.created_at,
               users.name,
               users.id,
               COALESCE(json_agg(subtasks.title), '[]') AS subtasks
                    FROM tasks
                    JOIN users ON tasks.user_id = users.id
                    LEFT JOIN subtasks ON tasks.id = subtasks.task_id
                    WHERE tasks.deleted_at IS NULL
                    GROUP BY tasks.id, users.id
        """)

        tasks_from_db = cur.fetchall()
        tasks = list()
        for task in tasks_from_db:
            tasks.append({
                "id": task[0],
                "title": task[1],
                "description": task[2],
                "status": task[3],
                "created_at": task[4],
                "user_name": task[5],
                "user_id": task[6],
                "subtasks": task[7],

            })
        return tasks


def get_task_by_user_id(user_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT tasks.id, tasks.title, tasks.description, tasks.status, tasks.created_at, users.name, users.id 
            FROM tasks 
            JOIN users ON tasks.user_id = users.id 
            WHERE tasks.deleted_at IS NULL and users.id = %s;
        """, (user_id,))

        tasks_from_db = cur.fetchall()
        if not tasks_from_db:
            return None

        tasks = []
        for task in tasks_from_db:
            tasks.append({
                "id": task[0],
                "title": task[1],
                "description": task[2],
                "status": task[3],
                "created_at": task[4],
                "user_name": task[5],
                "user_id": task[6],
            })
        return tasks

def create_new_task(user_id, title, describtion):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s) RETURNING id",
                    (user_id, title, describtion))
        task_id = cur.fetchone()[0]
        conn.commit()
        return task_id

def update_task(title, description, task_id, user_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            UPDATE tasks 
            SET title = %s, description = %s 
            WHERE id = %s AND user_id = %s AND deleted_at IS NULL 
            RETURNING id
        """, (title, description, task_id, user_id))
        task_id = cur.fetchone()[0]
        return task_id

def delete_task(task_id, user_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE tasks SET deleted_at = CURRENT_TIMESTAMP WHERE id = %s and user_id = %s RETURNING id;",
                    (task_id, user_id))
        task_id = cur.fetchone()[0]
        return task_id

def is_task_belongs_to_user(user_id, task_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute(" SELECT 1 FROM tasks WHERE id = %s AND user_id = %s", (task_id, user_id))
        return cur.fetchone() is not None

def create_subtask_by_task_id(task_id, title):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO subtasks (task_id, title) VALUES (%s, %s) RETURNING id;", (task_id, title))
        subtask_id = cur.fetchone()[0]
        conn.commit()
        return subtask_id


# ---------------------------------------------
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def check_password(password, hashed_password):
    if not hashed_password:
        return False
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register_user(name, email, password):
    hashed_password = hash_password(password)
    with connect_db() as conn, conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
            (name, email, hashed_password))
            user_id = cur.fetchone()[0]
            conn.commit()
            return user_id
        except psycopg2.Error as e:
            print(f"Ошибка при регистрации: {e}")
            return None

def login_user(email, password):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, password_hash FROM users WHERE email = %s;", (email,))
        user = cur.fetchone()

        if user and check_password(password, user[1]):
            access_token = create_access_token(identity=str(user[0]), expires_delta=timedelta(days=1))
            return access_token
        return None
# ---------------------------------------------
