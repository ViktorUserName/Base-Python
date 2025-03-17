SELECT version();


SELECT datname FROM pg_database;

SELECT current_database();

SELECT datname, pid, usename, application_name, state
FROM pg_stat_activity
WHERE datname = 'test2';

SELECT pg_terminate_backend(39648);


DROP DATABASE test3

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    Name CHARACTER VARYING(30),
    AGE INTEGER
);
INSERT INTO users (Name, AGE) VALUES ('Tom', 33);

SELECT * FROM users;