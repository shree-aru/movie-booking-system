
-- Create Database
CREATE DATABASE IF NOT EXISTS movie_booking_db;
USE movie_booking_db;

-- Table: Theatres
CREATE TABLE IF NOT EXISTS Theatres (
    theatre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    capacity INT NOT NULL
);

-- Table: Shows
CREATE TABLE IF NOT EXISTS Shows (
    show_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_title VARCHAR(255) NOT NULL,
    theatre_id INT NOT NULL,
    show_time DATETIME NOT NULL,
    ticket_price DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (theatre_id) REFERENCES Theatres(theatre_id)
);

-- Table: Seats
CREATE TABLE IF NOT EXISTS Seats (
    seat_id INT AUTO_INCREMENT PRIMARY KEY,
    theatre_id INT NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (theatre_id) REFERENCES Theatres(theatre_id)
);

-- Table: Customers
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20)
);

-- Table: Bookings
CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    show_id INT NOT NULL,
    seat_id INT NOT NULL,
    booking_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (show_id) REFERENCES Shows(show_id),
    FOREIGN KEY (seat_id) REFERENCES Seats(seat_id)
);


