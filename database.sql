CREATE DATABASE telemedicine;

USE telemedicine;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE symptoms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL
);