-- 1. Create Database
CREATE DATABASE IF NOT EXISTS event_ticket_db;
USE event_ticket_db;

-- 2. Create Events Table
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    venue VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    seats INT NOT NULL
);

-- 3. Create Bookings Table
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    event_id INT NOT NULL,
    ticket_count INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);
