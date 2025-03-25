import psycopg2
from datetime import datetime

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

def get_all_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT id, title, date FROM event ORDER BY date;
        """)
        events = cur.fetchall()
        return events

def add_event(title, date):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO event (title, date) VALUES (%s, %s)", (title, date))
        conn.commit()
        print('Event added.')

def change_event(event_id, title=None, date=None):
    with connect_db() as conn, conn.cursor() as cur:
        updates = []
        values = []

        if title:
            updates.append("title = %s")
            values.append(title)

        if date:
            date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S" )
            updates.append("date = %s")
            values.append(date_obj)

        if not updates:
            print("Нет изменений.")
            return

        values.append(event_id)
        query = f"UPDATE event SET {', '.join(updates)} WHERE id = %s"

        cur.execute(query, values)
        conn.commit()
        print("Событие успешно обновлено!")

def delete_event(event_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM event WHERE id = %s", (event_id,))
        conn.commit()

def get_seats(event_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT s.id, s.row_number, s.seat_number
            FROM Seats s
                LEFT JOIN Tickets t ON s.id = t.seat_id AND t.event_id = %s
                WHERE t.id IS NULL OR t.status = 'canceled';
            """, (event_id,))
        seats = cur.fetchall()
        return seats

def book_seat(row_number,seat_number, event_id):
    # ----- Проверка есть ли место
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM seats WHERE row_number = %s AND seat_number = %s"
                    , (row_number, seat_number))
        seat_id = cur.fetchone()

        if not seat_id:
            print('Такого места не существует')
            return

        seat_id = seat_id[0]
        # ------ проверка статуса
        cur.execute("""
            SELECT status FROM tickets WHERE seat_id = %s and event_id = %s;
        """, (seat_id, event_id))

        ticket_status = cur.fetchone()

        if ticket_status:
            if ticket_status[0] in ('booked', 'purchased'):
                print("Место уже забронировано или куплено!")
                return
            elif ticket_status[0] == 'used':
                print("Место уже использовано!")
                return
            elif ticket_status[0] == 'canceled':
                cur.execute("""
                    UPDATE tickets SET status = 'booked' WHERE seat_id = %s AND event_id = %s;
                """, (seat_id, event_id))
                print(f"Место {row_number}-{seat_number} успешно забронировано!")
        else:
            cur.execute("""
                INSERT INTO tickets (price, status, event_id, seat_id) 
                VALUES (200, 'booked', %s, %s);
            """, (event_id, seat_id))
            print(f"Место {row_number}-{seat_number} успешно забронировано!")

        conn.commit()

def unbook_seat(row_number,seat_number, event_id):
    with connect_db() as conn, conn.cursor() as cur:
        # Проверка на наличие такого места
        cur.execute("SELECT id FROM seats WHERE row_number = %s AND seat_number = %s"
                    , (row_number, seat_number))
        seat_id = cur.fetchone()
        if not seat_id:
            print('Такого места не существует')
            return
        seat_id = seat_id[0]
        # Проверка статуса
        cur.execute("""
                    SELECT status FROM tickets WHERE seat_id = %s and event_id = %s;
                """, (seat_id, event_id))

        ticket_status = cur.fetchone()

        if ticket_status:
            if ticket_status[0] == 'booked':
                cur.execute("UPDATE tickets SET status = 'canceled' WHERE seat_id = %s AND event_id = %s;",
                            (seat_id, event_id))
                conn.commit()
                print('Вы успешно отменили бронь!')
            elif ticket_status[0] == 'purchased':
                print('Место уже куплено, бронь не может быть отменена.')
            elif ticket_status[0] == 'used':
                print('Место уже использовано, бронь не может быть отменена.')
            elif ticket_status[0] == 'canceled':
                print('Бронь на это место уже отменена.')
        else:
            print('Место свободно, отмена не требуется.')

        conn.commit()

def search_event(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM event WHERE title ILIKE %s", (f"%{query}%",))
        events = cur.fetchall()

    if not events:
        print("События не найдены.")
        return []

    return events


