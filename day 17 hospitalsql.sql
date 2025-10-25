-- Create database
CREATE DATABASE IF NOT EXISTS hello;
USE hello;

-- Create Patients table
CREATE TABLE IF NOT EXISTS appt (
    idno CHAR(12) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender CHAR(1),
    phone CHAR(10),
    bg VARCHAR(5)
);

-- Create Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id CHAR(12) NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    room INT NOT NULL,
    appt_date DATE NOT NULL,
    appt_no INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES appt(idno) ON DELETE CASCADE
);

-- Optional: prevent duplicate appointment numbers for same doctor/date
CREATE UNIQUE INDEX uniq_doctor_date_no
ON appointments (doctor_name, appt_date, appt_no);
