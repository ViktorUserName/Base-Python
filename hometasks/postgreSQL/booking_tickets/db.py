import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'cinema',

}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Event (             
                id SERIAL PRIMARY KEY,
                title VARCHAR(30) NOT NULL,
                date TIMESTAMP NOT NULL
            );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS seats (
                id SERIAL PRIMARY KEY,
                row_number INT NOT NULL,
                seat_number INT NOT NULL,
            
                UNIQUE (row_number, seat_number)
        );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                price DECIMAL(10,2) NOT NULL,
                status TEXT CHECK (status IN ('booked', 'purchased', 'used', 'canceled')) DEFAULT 'booked' NOT NULL,
            
                event_id INT NOT NULL,
                seat_id INT NOT NULL,
            
                FOREIGN KEY (event_id) REFERENCES Event(id) ON DELETE CASCADE,
                FOREIGN KEY (seat_id) REFERENCES Seats(id) ON DELETE CASCADE,
            
                UNIQUE (event_id, seat_id)
                );
        """)
        conn.commit()
        print('Database initialized.')



def app():
    init_db()
    print('app started')

app()