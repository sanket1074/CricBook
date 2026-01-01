CREATE DATABASE cric_book;
USE cric_book;

CREATE TABLE users(
 id INT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(50),
 email VARCHAR(50),
 password VARCHAR(50),
 role VARCHAR(10)
);

CREATE TABLE matches(
 id INT PRIMARY KEY AUTO_INCREMENT,
 match_name VARCHAR(100),
 total_seats INT,
 available_seats INT
);

CREATE TABLE bookings(
 id INT PRIMARY KEY AUTO_INCREMENT,
 user_id INT,
 match_id INT,
 seats INT
);

INSERT INTO users VALUES(1,'Admin','admin@gmail.com','admin123','admin');

INSERT INTO matches (match_name, total_seats, available_seats) VALUES
('India vs Australia', 500, 500),
('India vs Pakistan', 800, 800),
('Chennai Super Kings vs Mumbai Indians', 600, 600),
('Royal Challengers Bangalore vs Kolkata Knight Riders', 550, 550),
('Delhi Capitals vs Rajasthan Royals', 450, 450);
SELECT * FROM users;

INSERT INTO users(name,email,password,role)
VALUES('Admin','admin@gmail.com','admin123','admin');

ALTER TABLE matches ADD price INT;
UPDATE matches SET price = 500 WHERE id > 0;
select * from matches;
