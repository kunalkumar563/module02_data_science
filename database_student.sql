CREATE DATABASE college_db;

USE college_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100),
    cgpa DECIMAL(3,2),
    email_id VARCHAR(100)
);

INSERT INTO students(name, subject, cgpa, email_id)
VALUES
('Kunal Kumar', 'Computer Science', 8.5, 'kunal@gmail.com'),
('Rahul Sharma', 'Math', 7.9, 'rahul@gmail.com'),
('Aman Singh', 'Physics', 8.1, 'aman@gmail.com'),
('Rohit Verma', 'Chemistry', 7.8, 'rohit@gmail.com'),
('Ankit Raj', 'Computer Science', 9.0, 'ankit@gmail.com');