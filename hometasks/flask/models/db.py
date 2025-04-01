import psycopg2
from datetime import datetime

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
            SELECT tasks.id, tasks.title, tasks.description, tasks.status, tasks.created_at, users.name 
            FROM tasks 
            JOIN users ON tasks.user_id = users.id 
            WHERE tasks.deleted_at IS NULL;
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

