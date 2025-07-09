
USE movie_booking_db;

-- Insert data into Theatres
INSERT INTO Theatres (name, location, capacity) VALUES
('Grand Cinema', 'Downtown', 150),
('Starplex', 'Mall Area', 200),
('City Cineplex', 'Uptown', 100);

-- Insert data into Shows
INSERT INTO Shows (movie_title, theatre_id, show_time, ticket_price) VALUES
('The Future Awaits', 1, '2025-07-10 18:00:00', 12.50),
('Mystery of the Old House', 2, '2025-07-10 19:30:00', 10.00),
('Comedy Night Live', 3, '2025-07-10 20:00:00', 15.00),
('The Future Awaits', 1, '2025-07-11 21:00:00', 12.50);

-- Insert data into Seats (assuming each theatre has seats A1-A10, B1-B10, etc. for simplicity)
-- For Grand Cinema (ID 1, capacity 150)
INSERT INTO Seats (theatre_id, seat_number, is_available) VALUES
(1, 'A1', TRUE), (1, 'A2', TRUE), (1, 'A3', TRUE), (1, 'A4', TRUE), (1, 'A5', TRUE),
(1, 'B1', TRUE), (1, 'B2', TRUE), (1, 'B3', TRUE), (1, 'B4', TRUE), (1, 'B5', TRUE);

-- For Starplex (ID 2, capacity 200)
INSERT INTO Seats (theatre_id, seat_number, is_available) VALUES
(2, 'C1', TRUE), (2, 'C2', TRUE), (2, 'C3', TRUE), (2, 'C4', TRUE), (2, 'C5', TRUE),
(2, 'D1', TRUE), (2, 'D2', TRUE), (2, 'D3', TRUE), (2, 'D4', TRUE), (2, 'D5', TRUE);

-- For City Cineplex (ID 3, capacity 100)
INSERT INTO Seats (theatre_id, seat_number, is_available) VALUES
(3, 'E1', TRUE), (3, 'E2', TRUE), (3, 'E3', TRUE), (3, 'E4', TRUE), (3, 'E5', TRUE),
(3, 'F1', TRUE), (3, 'F2', TRUE), (3, 'F3', TRUE), (3, 'F4', TRUE), (3, 'F5', TRUE);

-- Insert data into Customers
INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES
('Alice', 'Smith', 'alice.smith@example.com', '111-222-3333'),
('Bob', 'Johnson', 'bob.johnson@example.com', '444-555-6666'),
('Charlie', 'Brown', 'charlie.brown@example.com', '777-888-9999');

-- Insert data into Bookings (example bookings)
-- Alice books a seat for 'The Future Awaits' at Grand Cinema
INSERT INTO Bookings (customer_id, show_id, seat_id, booking_time) VALUES
(1, 1, 1, '2025-07-09 10:00:00');

-- Bob books a seat for 'Mystery of the Old House' at Starplex
INSERT INTO Bookings (customer_id, show_id, seat_id, booking_time) VALUES
(2, 2, 11, '2025-07-09 11:30:00');

-- Charlie books a seat for 'Comedy Night Live' at City Cineplex
INSERT INTO Bookings (customer_id, show_id, seat_id, booking_time) VALUES
(3, 3, 21, '2025-07-09 12:00:00');

-- Update seat availability after booking
UPDATE Seats SET is_available = FALSE WHERE seat_id IN (1, 11, 21);


