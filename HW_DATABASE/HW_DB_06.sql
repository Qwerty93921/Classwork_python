------------------------------------------------------------------------------------------------

--HW 6

--Работа с базой данных из прошлого ДЗ

ALTER TABLE Faculties
ADD Dean nvarchar(50) NOT NULL DEFAULT ''

select * from Faculties
------------------------------------------------------------------------------------------------

ALTER TABLE Teachers
ADD 
IsAssistant bit NOT NULL DEFAULT 0,
IsProfessor bit NOT NULL DEFAULT 0,
Position nvarchar(50) NOT NULL DEFAULT ''

select * from Teachers

------------------------------------------------------------------------------------------------

--1
--Обратный порядок

SELECT *  from Departments
ORDER BY Id DESC

--2

select * from Groups

select Name, Rating from Groups

--3

select * from Teachers

select Surname, Premium + Salary from Teachers

--4

select * from Faculties

INSERT INTO Faculties(Dean)
VALUES
('Mark'),
('Josh'),
('Kevin'),
('Molly'),
('Dinny')

--UPDATE Faculties
--SET Dean = 'Donald'
--WHERE Id = 5;

SELECT
    'The dean of faculty ' + Name + ' is ' + Dean + '.' AS FormattedOutput
FROM
    Faculties;

--5

select * from Teachers

--UPDATE Teachers
--SET IsProfessor = 1 WHERE Id = 11

SELECT Surname from Teachers
WHERE IsProfessor = 1 AND Salary > 1050

--UPDATE Teachers
--SET Salary = 1500 WHERE Id = 11

--6

select * from Departments

select Name from Departments
WHERE Financing < 11000 OR Financing > 25000

--7

SELECT * from Faculties

--INSERT INTO Faculties(Name, Dean)
--VALUES('Computer Science', 'Jonatan')

select Name from Faculties
WHERE Name != 'Computer Science'

--8

SELECT * FROM Teachers

SELECT Surname, Position FROM Teachers
WHERE IsProfessor = 0

--9

select * from Teachers

SELECT Surname, Position, Salary, Premium FROM Teachers
WHERE Premium BETWEEN 160 AND 550

--10

select * from Teachers

--UPDATE Teachers
--SET IsAssistant = 1 WHERE Id = 13

SELECT Surname, Salary FROM Teachers
WHERE IsAssistant = 1

--11

select * from Teachers

SELECT Surname, Position from Teachers
WHERE EmploymentDate < '2000-01-01'

--12

SELECT * FROM Departments

SELECT Name FROM Departments

--INSERT INTO Departments(Name)
--VALUES('Software Development')

SELECT Name AS "Name of Department"
FROM Departments
WHERE Name < 'Software Development'
ORDER BY Name;

--13

SELECT * FROM Teachers

SELECT Surname FROM Teachers
WHERE IsAssistant = 1 AND Premium + Salary <= 1200

--14

SELECT * FROM Groups

SELECT Name FROM Groups
WHERE Year = 5 AND Rating BETWEEN 2 AND 4

--INSERT INTO Groups(Name, Rating, Year)
--VALUES('DELTA', 4, 5)

--15

SELECT * FROM Teachers

SELECT Surname FROM Teachers
WHERE Salary < 550 OR Premium < 200
