import psycopg2

connect = psycopg2.connect(
    dbname="metanit_learn",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = connect.cursor()



cursor.execute("""
    UPDATE employees
    SET HireDate = '2000-03-17'
    WHERE Salary > 105000;
""")
connect.commit()

cursor.execute('SELECT * FROM employees')
cursor.execute('SELECT * from employees ORDER BY Id')


rows = cursor.fetchall()

for row in rows:
    print(row)
