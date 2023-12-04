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
