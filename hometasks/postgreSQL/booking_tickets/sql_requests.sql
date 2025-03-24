CREATE TABLE Event
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    date TIMESTAMP NOT NULL
);


CREATE TABLE Seats
(
    id SERIAL PRIMARY KEY,
    row_number INT NOT NULL,
    seat_number INT NOT NULL,

    UNIQUE (row_number, seat_number)

--     event_id INT,
--     FOREIGN KEY (event_id) REFERENCES Event(id) ON DELETE CASCADE
);

CREATE TABLE Tickets
(
    id SERIAL PRIMARY KEY,
    price DECIMAL(10,2) NOT NULL,
    status TEXT CHECK (status IN ('booked', 'purchased', 'used', 'canceled')) DEFAULT 'booked' NOT NULL,

    event_id INT NOT NULL,
    seat_id INT NOT NULL,

    FOREIGN KEY (event_id) REFERENCES Event(id) ON DELETE CASCADE,
    FOREIGN KEY (seat_id) REFERENCES Seats(id) ON DELETE CASCADE,

    UNIQUE (event_id, seat_id)
);

INSERT INTO Event(title, date)
VALUES
('Матрица', '2025-03-28 18:00:00'),
('Матрица', '2025-03-28 21:00:00');

INSERT INTO Seats(row_number, seat_number)
VALUES
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5);

INSERT INTO Tickets (price, status, event_id, seat_id)
VALUES
(500.00, 'booked', 1, 1),  -- Место 1,1
(500.00, 'booked', 1, 2),  -- Место 1,2
(500.00, 'purchased', 1, 3); -- Место 1,3 уже куплено

SELECT * FROM Event;
SELECT * FROM Seats;
SELECT * FROM Tickets;

SELECT Tickets.id, Tickets.price, Tickets.status,
       Event.title, Event.date
from Tickets
RIGHT JOIN Event
ON Tickets.event_id = Event.id
