CREATE DATABASE homework

CREATE TABLE employees
(
    Id SERIAL PRIMARY KEY,
    Name CHARACTER VARYING(30) NOT NULL,
    Position CHARACTER VARYING(30) NOT NULL,
    Department CHARACTER VARYING(30) NOT NULL,
    Salary INTEGER NOT NULL
);

INSERT INTO employees (Name, Position, Department, Salary) VALUES
('Иван Петров', 'Разработчик', 'IT', 120000),
('Мария Сидорова', 'Бухгалтер', 'Финансы', 90000),
('Алексей Смирнов', 'Менеджер', 'Продажи', 110000),
('Ольга Кузнецова', 'HR', 'Кадры', 85000),
('Дмитрий Иванов', 'Аналитик', 'Аналитика', 100000);


UPDATE  employees
set Position =  'Разработчик бека'
WHERE  Position = 'Разработчик';

SELECT * from employees ORDER BY Id;

ALTER TABLE employees
ADD HireDate DATE NOT NULL DEFAULT CURRENT_DATE;

UPDATE employees
set HireDate = '2022-03-17'
WHERE Salary > 105000;

SELECT * from employees
WHERE Position = 'Менеджер';

DROP FUNCTION IF EXISTS get_employees_by_position(VARCHAR);


-- функция по поимку позиции в позиции
CREATE OR REPLACE FUNCTION get_employees_by_position(dept_position VARCHAR)
RETURNS SETOF employees AS $$
BEGIN
    RETURN QUERY SELECT * FROM employees WHERE Position = dept_position;
END;
$$ LANGUAGE plpgsql;



SELECT proname FROM pg_proc WHERE proname = 'get_employees_by_position';


SELECT * FROM get_employees_by_position('Менеджер');

SELECT * from employees
WHERE Salary>95000;

-- функция фильтра по заданной зарплате
CREATE OR REPLACE FUNCTION get_employees_by_salary(dept_salary INTEGER)
RETURNS SETOF employees AS $$
BEGIN
    RETURN QUERY SELECT * FROM employees WHERE employees.Salary > dept_salary;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_employees_by_salary(101000);

SELECT * from employees
WHERE Department = 'Продажи';

--тоже самое функция
CREATE OR REPLACE FUNCTION get_employees_by_department(dept_department VARCHAR)
RETURNS SETOF employees AS $$
BEGIN
    RETURN QUERY SELECT * FROM employees WHERE Department = dept_department;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_employees_by_department('Продажи');


SELECT  Avg(Salary) from employees;
