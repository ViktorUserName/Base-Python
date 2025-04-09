CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
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

CREATE TABLE subtasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    status TEXT CHECK (status IN ('done', 'not done')) DEFAULT 'not done' NOT NULL,

    task_id INT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE task_tags (
    id SERIAL PRIMARY KEY,
    task_id INT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- Добавляем пользователей
INSERT INTO users (name, email, password_hash)
VALUES
    ('Alice', 'alice@example.com', 'hashed_password_1'),
    ('Bob', 'bob@example.com', 'hashed_password_2');

-- Добавляем задачи
INSERT INTO tasks (title, description, status, user_id)
VALUES
    ('Купить продукты', 'Купить молоко, хлеб и яйца', 'new', 1),
    ('Прочитать книгу', 'Закончить 3-ю главу', 'in progress', 2);

-- Добавляем подзадачи
INSERT INTO subtasks (title, status, task_id)
VALUES
    ('Купить молоко', 'not done', 1),
    ('Прочитать 10 страниц', 'not done', 2);

-- Добавляем теги
INSERT INTO tags (name)
VALUES
    ('важное'),
    ('работа');

-- Добавляем связи задач с тегами
INSERT INTO task_tags (task_id, tag_id)
VALUES
    (1, 1),
    (2, 2);
