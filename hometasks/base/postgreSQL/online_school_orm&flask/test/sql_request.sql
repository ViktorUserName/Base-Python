CREATE TABLE disciplies
(
    id SERIAL PRIMARY KEY,
    title varchar(30)
);

CREATE TABLE students
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    last_name VARCHAR(30)
);

CREATE TABLE teachers
(
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(30)
);

CREATE TABLE disciple_student
(
    id SERIAL PRIMARY KEY,
    disciple_id INT,
    student_id INT,
    FOREIGN KEY (disciple_id) REFERENCES disciplies(id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

CREATE TABLE teacher_disciple
(
    id SERIAL PRIMARY KEY,
    disciple_id INT,
    teacher_id INT,
    FOREIGN KEY (disciple_id) REFERENCES disciplies(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE
);

CREATE TABLE grades
(
    id SERIAL PRIMARY KEY,
    grade INT CHECK (grade BETWEEN 1 AND 10),
    date DATE NOT NULL DEFAULT CURRENT_DATE CHECK ( date <= CURRENT_DATE),

    student_id INT,
    disciple_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (disciple_id) REFERENCES disciplies(id) ON DELETE CASCADE
);

INSERT INTO disciplies (title) VALUES
('Физика'),
('Русский'),
('Математика');

INSERT INTO students (name, last_name) VALUES
('Иван', 'Иванов'),
('Петр', 'Петров'),
('Алексей', 'Алексеев'),
('Мария', 'Мариева'),
('Екатерина', 'Екатерина');

INSERT INTO teachers (last_name) VALUES
('Смирнов'),  -- учитель физики
('Кузнецова'), -- учитель русского
('Попов'); -- учитель математики

INSERT INTO disciple_student (disciple_id, student_id)
VALUES
(1, 1),
(1, 4),
(1, 5);

INSERT INTO disciple_student (disciple_id, student_id)
VALUES
(2, 2),
(2, 3),
(2, 5);

INSERT INTO disciple_student (disciple_id, student_id)
VALUES
(3, 1),
(3, 2),
(3, 3),
(3, 4);

INSERT INTO teacher_disciple (disciple_id, teacher_id)
VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO grades (grade, date, student_id, disciple_id) VALUES
(8, '2025-03-01', 1, 1),  -- Иванов получил 8 по Физике 1 марта
(6, '2025-03-10', 1, 1),  -- Иванов получил 6 по Физике 10 марта
(7, '2025-03-05', 4, 1),  -- Мариева получила 7 по Физике 5 марта

(9, '2025-03-02', 2, 2),  -- Петров получил 9 по Русскому 2 марта
(5, '2025-03-12', 3, 2),  -- Алексеев получил 5 по Русскому 12 марта
(8, '2025-03-14', 5, 2),  -- Екатерина получила 8 по Русскому 14 марта

(10, '2025-03-03', 1, 3), -- Иванов получил 10 по Математике 3 марта
(7, '2025-03-08', 2, 3),  -- Петров получил 7 по Математике 8 марта
(6, '2025-03-15', 3, 3),  -- Алексеев получил 6 по Математике 15 марта
(8, '2025-03-18', 4, 3);  -- Мариева получила 8 по Математике 18 марта


SELECT t.last_name, d.title FROM teacher_disciple t_d
left join teachers t on t_d.teacher_id = t.id
left join disciplies d on t_d.disciple_id = d.id;

SELECT s.name, d.title, g.grade, g.date
FROM disciple_student d_s
LEFT JOIN students s ON d_s.student_id = s.id
LEFT JOIN disciplies d ON d_s.disciple_id = d.id
LEFT JOIN grades g ON d_s.student_id = g.student_id AND d_s.disciple_id = g.disciple_id
WHERE s.name = 'Иван' AND d.title = 'Физика'
;
SELECT s.name, d.title, g.grade, g.date
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN disciplies d ON g.disciple_id = d.id
WHERE s.name = 'Иван' AND d.title = 'Физика';

SELECT g.date, g.grade, d.title, s.name FROM grades g
inner join disciplies d on d.id = g.disciple_id
inner join students s on g.student_id = s.id WHERE d.title = 'Физика'
