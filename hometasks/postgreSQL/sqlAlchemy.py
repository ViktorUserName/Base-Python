from sqlalchemy import create_engine, text, result_tuple

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/metanit_learn"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM employees ORDER BY Id "))
    for row in result:
        print(row)