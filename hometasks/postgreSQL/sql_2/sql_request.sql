CREATE TABLE Authors
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE Books
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE
);

CREATE TABLE Sales
(
    id SERIAL PRIMARY KEY,
    quantity INT,
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES Books(id) ON DELETE CASCADE
);

INSERT INTO Authors (first_name, last_name) VALUES
('Stephen', 'King'),
('J.K.', 'Rowling'),
('George', 'Orwell'),
('Agatha', 'Christie'),
('Leo', 'Tolstoy');

INSERT INTO Books (title, author_id) VALUES
('1984', 3),
('Animal Farm', 3),
('Harry Potter', 2),
('Murder on the Orient Express', 4),
('War and Peace', 5);

INSERT INTO Books (title) VALUES
('hero of world');

INSERT INTO sales (quantity, book_id) VALUES
(150, 1),  -- Продажи "1984"
(200, 2),  -- Продажи "Animal Farm"
(300, 3),  -- Продажи "Harry Potter"
(180, 4),  -- Продажи "Murder on the Orient Express"
(120, 5);  -- Продажи "War and Peace"


SELECT  * FROM Authors
    INNER JOIN Books
    ON Authors.id = Books.author_id;

---  |
---  |
---  |
---  ↓ --- только нужные селекты

SELECT Authors.first_name, Authors.last_name, Books.title FROM Authors
    INNER JOIN Books
        ON Authors.id = Books.author_id;

SELECT Authors.first_name, Authors.last_name, Books.title FROM Authors
    LEFT JOIN Books
        ON Authors.id = Books.author_id;

SELECT Authors.first_name, Authors.last_name, Books.title FROM Authors
    RIGHT JOIN Books
        ON Authors.id = Books.author_id;

--- Дальше задание 3 множественные join

SELECT A.first_name, A.last_name, B.title, S.quantity FROM Authors A
    INNER JOIN Books B
    on A.id = B.author_id
    INNER JOIN Sales S
    on B.id = S.book_id;

SELECT A.first_name, A.last_name, B.title, S.quantity FROM Authors A
    LEFT JOIN  Books B
    on A.id = B.author_id
    LEFT JOIN Sales S
    on B.id = S.book_id;

SELECT A.first_name, A.last_name, B.title, S.quantity FROM Authors A
    RIGHT JOIN  Books B
    on A.id = B.author_id
    RIGHT JOIN Sales S
    on B.id = S.book_id;

--- Агрегация

SELECT A.first_name, A.last_name, SUM(S.quantity) AS total_sell
FROM Authors A
INNER JOIN Books B on A.id = B.author_id
INNER JOIN Sales S on B.id = S.book_id
GROUP BY A.id;

SELECT A.first_name, A.last_name, SUM(S.quantity) AS total_sell
FROM Authors A
LEFT JOIN Books B on A.id = B.author_id
LEFT JOIN Sales S on B.id = S.book_id
GROUP BY A.id;


--- подзапросы и join

SELECT A.first_name, A.last_name, SUM(S.quantity) AS total_sell FROM Authors A
    INNER JOIN Books B ON A.id = B.author_id
    INNER JOIN Sales S ON B.id = S.book_id
    GROUP BY A.id
        HAVING SUM(S.quantity) = (SELECT MAX(total_sell)
                          FROM (SELECT B.author_id, SUM(S.quantity) AS total_sales
                                FROM Books B
                                INNER JOIN Sales S ON B.id = S.book_id
                                GROUP BY B.author_id) AS subquery);