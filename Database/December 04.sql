select * from Customers;

ALTER TABLE Customers
ADD Email nvarchar(100)

select * from Customers
where Email is not null

--Смена почты у пользователя Alfred

update Customers
set Email = 'newemail@mail.com'
where CompanyName = 'Alfreds Futterkiste'

--ALTER нужен для РЕДАКТИРОВАНИЯ

--Выбрать таблицу для редактирования
--Выбрать команду и часть таблицы для редактирования

ALTER TABLE Customers
DROP COLUMN Email

--------------------------------------------------------------------------------

--Создание базы данных

CREATE DATABASE Hospital;
USE Hospital;

--Создание таблицы Departments

CREATE TABLE Departments (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	Building INT NOT NULL CHECK (Building >= 1 AND BUILDING <= 5),
	Name VARCHAR(100) NOT NULL UNIQUE
)

--Вставка данных в таблицу "Departments"
--TRUNCATE, DELETE, DROP

--DROP удаляет ВСЮ БАЗУ ДАННЫХ
--DELETE удаляет данные внутри таблицы
--TRUNCATE удаляет данные и файлы внутри таблицы

--DELETE Departments(название таблицы)

INSERT INTO Departments (Building, Name) VALUES
	(1, 'Cardiology'),
	(2, 'Neurology'),
	(3, 'Orthopedics'),
	(4, 'Oncology'),
	(5, 'Pediatrics')

select * from Departments

--------------------------------------------------------------------------------

-- Создание базы данных


CREATE DATABASE Hospital;
USE Hospital;

--коммент


-- Создание таблицы "Departments"
CREATE TABLE Departments (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Building INT NOT NULL CHECK (Building >= 1 AND Building <= 5),
    Name NVARCHAR(100) NOT NULL UNIQUE,
);

-- Вставка данных в таблицу "Departments"
INSERT INTO Departments (Building, Name) VALUES
    (1, 'Cardiology'),
    (2, 'Neurology'),
    (3, 'Orthopedics'),
    (4, 'Oncology'),
    (5, 'Pediatrics');

select * from Departments;




-- Создание таблицы "Doctors"
CREATE TABLE Doctors (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(MAX) NOT NULL,
    Premium MONEY NOT NULL DEFAULT 0 CHECK (Premium >= 0),
    Salary MONEY NOT NULL CHECK (Salary > 0),
    Surname NVARCHAR(MAX) NOT NULL,
);

SELECT * from Doctors

-- Вставка данных в таблицу "Doctors"
INSERT INTO Doctors (Name, Premium, Salary, Surname) VALUES
    ('John', 500, 6000, 'Doe'),
    ('Alice', 300, 5500, 'Smith'),
    ('Bob', 200, 5000, 'Johnson'),
    ('Eva', 400, 7000, 'Williams'),
    ('Michael', 600, 8000, 'Brown'),
    ('Sophia', 350, 6000, 'Jones'),
    ('Daniel', 450, 7500, 'Taylor'),
    ('Olivia', 250, 5500, 'White'),
    ('Matthew', 550, 7200, 'Anderson'),
    ('Emily', 300, 5800, 'Clark'),
    ('David', 400, 6200, 'Hill'),
    ('Ava', 500, 7000, 'Baker'),
    ('Christopher', 350, 6500, 'Miller'),
    ('Emma', 200, 5000, 'Turner'),
    ('Liam', 450, 6800, 'Ward');


select * from Doctors;

-- Создание таблицы "Examinations"
CREATE TABLE Examinations (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL UNIQUE,
);

-- Вставка данных в таблицу "Examinations"
INSERT INTO Examinations (Name) VALUES
    ('Blood Test'),
    ('MRI Scan'),
    ('X-ray'),
    ('Ultrasound'),
    ('CT Scan'),
    ('EKG'),
    ('Colonoscopy'),
    ('Endoscopy'),
    ('Biopsy'),
    ('Bone Density Test'),
    ('Eye Exam'),
    ('Allergy Test'),
    ('Pregnancy Test'),
    ('Cholesterol Test'),
    ('Thyroid Function Test');




-- Создание таблицы "Wards"
CREATE TABLE Wards (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(20) NOT NULL UNIQUE,
    Places INT NOT NULL CHECK (Places >= 1),
    DepartmentId INT NOT NULL FOREIGN KEY REFERENCES Departments(Id),
);

-- Вставка данных в таблицу "Wards"
INSERT INTO Wards (Name, Places, DepartmentId) VALUES
    ('Ward A', 10, 1),
    ('Ward B', 12, 2),
    ('Ward C', 8, 3),
    ('Ward D', 15, 4),
    ('Ward E', 20, 5);

select * from Wards

-- Создание таблицы "DoctorsExaminations"
CREATE TABLE DoctorsExaminations (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    EndTime TIME NOT NULL /*CHECK (EndTime > StartTime)*/,
    StartTime TIME NOT NULL /*CHECK (StartTime >= '08:00' AND StartTime <= '18:00')*/,
    DoctorId INT NOT NULL FOREIGN KEY REFERENCES Doctors(Id),
    ExaminationId INT NOT NULL FOREIGN KEY REFERENCES Examinations(Id),
    WardId INT NOT NULL FOREIGN KEY REFERENCES Wards(Id),
);

ALTER TABLE DoctorsExaminations
ADD CONSTRAINT CHK_EndTime CHECK (EndTime > StartTime);


-- Вставка данных в таблицу "DoctorsExaminations"
INSERT INTO DoctorsExaminations (EndTime, StartTime, DoctorId, ExaminationId, WardId) VALUES
    ('10:00', '08:30', 1, 1, 1),
    ('11:30', '09:00', 2, 2, 2),
    ('13:00', '10:30', 3, 3, 3),
    ('14:30', '11:00', 4, 4, 4),
    ('16:00', '12:30', 5, 5, 5),
    ('17:30', '13:00', 6, 6, 1),
    ('10:30', '08:00', 7, 7, 2),
    ('12:00', '09:30', 8, 8, 3),
    ('13:30', '10:00', 9, 9, 4),
    ('15:00', '11:30', 10, 10, 5),
    ('16:30', '12:00', 11, 11, 1),
    ('18:00', '13:30', 12, 12, 2),
    ('11:00', '08:30', 13, 13, 3),
    ('12:30', '09:00', 14, 14, 4),
    ('14:00', '10:30', 15, 15, 5);

select * from DoctorsExaminations;

-- ----------------------------------------------------------------------------------------------------

-- 1 task

select * from Wards
WHERE Places > 10

-- Решение

SELECT COUNT(*) AS NumberOfWards
from Wards
WHERE Places > 10

-- 2 task

select Departments.Name, Wards.Places
from Departments
join Wards on Departments.Id = Wards.Id

-- 3 task

select Departments.Name, Wards.Places
from Departments
join Wards on Departments.Id = Wards.Id

--task 8

select Name as WardName
from Wards
WHERE Places =
(SELECT MIN(Places) FROM Wards)

Select top 1 name as wardname, Places
from wards
order by Places
/*
1. Отделения (Departments)
■ Идентификатор (Id). Уникальный идентификатор отделения.
▷ Тип данных — int.
▷ Авто приращение.
▷ Не может содержать null-значения.
▷ Первичный ключ.

3
Практическое задание № 5
■ Корпус (Building). Номер корпуса, в котором располагается отделение.
▷ Тип данных — int.
▷ Не может содержать null-значения.
▷ Должно быть в диапазоне от 1 до 5.
■ Название (Name). Название отделения.
▷ Тип данных — nvarchar(100).
▷ Не может содержать null-значения.
▷ Не может быть пустым.
▷ Должно быть уникальным.
2. Врачи (Doctors)
■ Идентификатор (Id). Уникальный идентификатор врача.
▷ Тип данных — int.
▷ Авто приращение.
▷ Не может содержать null-значения.
▷ Первичный ключ.
■ Имя (Name). Имя врача.
▷ Тип данных — nvarchar(max).
▷ Не может содержать null-значения.
▷ Не может быть пустым.
■ Надбавка (Premium). Надбавка врача.
▷ Тип данных — money.
▷ Не может содержать null-значения.
▷ Не может быть меньше 0.
▷ Значение по умолчанию — 0.
■ Ставка (Salary). Ставка врача.
4
Практическое задание № 5
▷ Тип данных — money.
▷ Не может содержать null-значения.
▷ Не может быть меньше либо равно 0.
■ Фамилия (Surname). Фамилия врача.
▷ Тип данных — nvarchar(max).
▷ Не может содержать null-значения.
▷ Не может быть пустым.
3. Врачи и обследования (DoctorsExaminations)
■ Идентификатор (Id). Уникальный идентификатор врача
и обследования.
▷ Тип данных — int.
▷ Авто приращение.
▷ Не может содержать null-значения.
▷ Первичный ключ.
■ Время завершения (EndTime). Время завершения обследования.
▷ Тип данных — time.
▷ Не может содержать null-значения.
▷ Должно быть больше времени начала обследования.
■ Время начала (StartTime). Время начала обследования.
▷ Тип данных — time.
▷ Не может содержать null-значения.
▷ Должно быть в диапазоне от 8:00 до 18:00.
■ Идентификатор врача (DoctorId). Врач.
▷ Тип данных — int.
▷ Не может содержать null-значения.
5
Практическое задание № 5
▷ Внешний ключ.
■ Идентификатор обследования (ExaminationId). Обследование.
▷ Тип данных — int.
▷ Не может содержать null-значения.
▷ Внешний ключ.
■ Идентификатор палаты (WardId). Палата.
▷ Тип данных — int.
▷ Не может содержать null-значения.
▷ Внешний ключ.
4. Обследования (Examinations)
■ Идентификатор (Id). Уникальный идентификатор обследования.
▷ Тип данных — int.
▷ Авто приращение.
▷ Не может содержать null-значения.
▷ Первичный ключ.
■ Название (Name). Название обследования.
▷ Тип данных — nvarchar(100).
▷ Не может содержать null-значения.
▷ Не может быть пустым.
▷ Должно быть уникальным.
5. Палаты (Wards)
■ Идентификатор (Id). Уникальный идентификатор палаты.
▷ Тип данных — int.
▷ Авто приращение.
6
Практическое задание № 5
▷ Не может содержать null-значения.
▷ Первичный ключ.
■ Название (Name). Название палаты.
▷ Тип данных — nvarchar(20).
▷ Не может содержать null-значения.
▷ Не может быть пустым.
▷ Должно быть уникальным.
■ Места (Places). Количество мест в палате.
▷ Тип данных — int.
▷ Не может содержать null-значения.
▷ Не может быть меньше 1.
■ Идентификатор отделения (DepartmentId). Отделение,
в котором располагается палата.
▷ Тип данных — int.
▷ Не может содержать null-значения.
▷ Внешний ключ.
*/