CREATE TABLE Teachers(
	Id int PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	EmploymentDate date NOT NULL CHECK(EmploymentDate >= '1990-01-01'),
	Name nvarchar(50) NOT NULL,
	Surname nvarchar(50) NOT NULL,
	Premium money NOT NULL DEFAULT 0 CHECK(Premium >= 0),
	Salary money NOT NULL CHECK(Salary > 0)
)

select * from Teachers

------------------------------------------------------------------------------------------------

CREATE TABLE Groups(
	Id int PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	Name nvarchar(10) NOT NULL UNIQUE,
	Rating int NOT NULL CHECK(Rating >= 0 AND Rating <= 5),
	Year int NOT NULL CHECK(Year >= 1 AND Year <= 5)
)

select * from Groups

------------------------------------------------------------------------------------------------

CREATE TABLE Departments(
	Id int PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	Financing money NOT NULL CHECK(Financing >= 0) DEFAULT 0,
	Name nvarchar(100) NOT NULL UNIQUE
)

select * from Departments

------------------------------------------------------------------------------------------------

CREATE TABLE Faculties(
	Id int PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	Name nvarchar(100) NOT NULL UNIQUE
)

select * from Faculties

------------------------------------------------------------------------------------------------

--Добавление данных

INSERT INTO Teachers(EmploymentDate, Name, Surname, Premium, Salary)
VALUES
('2022-01-19', 'John', 'Smith', 0, 300),
('2023-05-15', 'Samanta', 'Barbara', 200, 400),
('2020-03-25', 'Alex', 'Winish', 100, 300),
('2022-07-28', 'Sam', 'Mow', 0, 200)

select * from Teachers

--Delete from Teachers WHERE Name = 'John' AND Surname = 'Smith'
--DELETE FROM Teachers

------------------------------------------------------------------------------------------------

INSERT INTO Groups(Name, Rating, Year)
VALUES
('ALPHA', 5, 5),
('BETA', 4, 3),
('GAMMA', 3, 1)

select * from Groups

------------------------------------------------------------------------------------------------

INSERT INTO Departments(Financing, Name)
VALUES
(2000, 'Physics'),
(500, 'PE'),
(1500, 'Math'),
(3000, 'Chemistry')

select * from Departments

------------------------------------------------------------------------------------------------

INSERT INTO Faculties(Name)
VALUES
('Marketing'),
('Sports'),
('Management'),
('High math'),
('History')

select * from Faculties

------------------------------------------------------------------------------------------------

--Итоговые таблицы

select * from Teachers
select * from Groups
select * from Departments
select * from Faculties
