--1 Таблица
--Пользователи

CREATE TABLE Users(
	Id int PRIMARY KEY IDENTITY(1, 1) NOT NULL,
	Name nvarchar(50),
	Surname nvarchar(50),
	SubscribeStatus bit DEFAULT 0
)

ALTER TABLE Users
ADD AutoRenewSubscribeStatus bit

INSERT INTO Users(Name, Surname, SubscribeStatus, AutoRenewSubscribeStatus)
VALUES
('Alex', 'Mith', 1, 1),
('George', 'Washington', 1, 1),
('Josh', 'Winston', 1, 1),
('Margaret', 'Miller', 1, 0),
('John', 'Second', 0, 0),
('Donald', 'Vin', 1, 1),
('User_7', 'Seven', 1, 1),
('User_8', 'Eight', 1, 0),
('User_9', 'Nine', 0, 0),
('User_10', 'Ten', 1, 1),
('User_11', 'Eleven', 1, 1),
('User_12', 'Twelve', 1, 1),
('User_13', 'Thirteen', 1, 0),
('User_14', 'Fourteen', 0, 0),
('User_15', 'Fifteen', 1, 1)

SELECT * FROM Users

---------------------------------------------------------------------------------------------

--2 Таблица
--Тип подписки

CREATE TABLE SubscribeType(
	Id int PRIMARY KEY IDENTITY(1, 1),
	DefaultSub bit DEFAULT 0,
	PremiumSub bit DEFAULT 0,
	GoldSub bit DEFAULT 0
)

ALTER TABLE SubscribeType
ADD NoSub bit DEFAULT 1

SELECT * FROM SubscribeType

INSERT INTO SubscribeType(DefaultSub, PremiumSub, GoldSub, NoSub)
VALUES
(1, 0, 0, 0),
(0, 0, 1, 0),
(0, 1, 0, 0),
(0, 0, 0, 1),
(0, 0, 1, 0),
(0, 0, 1, 0),
(1, 0, 0, 0),
(0, 1, 0, 0),
(0, 0, 0, 1),
(0, 0, 1, 0),
(1, 0, 0, 0),
(0, 1, 0, 0),
(0, 1, 0, 0),
(0, 0, 0, 1),
(1, 0, 0, 0)

SELECT * FROM SubscribeType

---------------------------------------------------------------------------------------------

--Таблица 3

--Заказов в месяц и доход в месяц
--1 Order - 100


--CAST(AmountOfOrders * 100 AS money)
--CAST (expression AS data_type)


CREATE TABLE StatsPerMonth(
	Id int PRIMARY KEY IDENTITY(1, 1),
	AmountOfOrders int DEFAULT 0,
	EarningsFromClient AS CAST(AmountOfOrders * 100 AS money)
)

SELECT * FROM StatsPerMonth

INSERT INTO StatsPerMonth(AmountOfOrders)
VALUES
(5),
(3),
(5),
(4),
(5),
(4),
(1),
(8),
(7),
(3),
(4),
(7),
(5),
(10),
(2)


--Временная таблица которая показывает имя и фамилию пользователя и его доход компании в месяц, и соединяет одинаковые ID c двух таблиц
Select Users.Name, Users.Surname ,StatsPerMonth.EarningsFromClient
FROM Users
INNER JOIN StatsPerMonth ON Users.Id = StatsPerMonth.Id

---------------------------------------------------------------------------------------------
--4 Таблица
--Личные данные пользователей

CREATE TABLE UserData(Id int PRIMARY KEY IDENTITY(1, 1), PhoneNumber varchar(20) UNIQUE, Password varchar(30), Age int CHECK(Age <= 100 AND Age >= 18))

SELECT * FROM UserData

--DROP TABLE UserData

INSERT INTO UserData(PhoneNumber, Password, Age)
VALUES
(81289282928, 'qwerty123', 42),
(12345678901, 'qwerty124', 25),
(09876543210, 'qwerty125', 18),
(82712847123, 'qwerty126', 42),
(47128123598, 'qwerty127', 47),
(89126123853, 'qwerty128', 45),
(12835748323, 'qwerty129', 23),
(48328761235, 'qwerty130', 37),
(58371298743, 'qwerty131', 55),
(29237128731, 'qwerty132', 89),
(89271264712, 'qwerty133', 71),
(21827827138, 'qwerty134', 35),
(21389854798, 'qwerty135', 28),
(23784879232, 'qwerty136', 51),
(27389621763, 'qwerty137', 50)

SELECT * FROM UserData

---------------------------------------------------------------------------------------------

--5 Таблица
--Местоположение пользователей

CREATE TABLE UsersLocation(Id int PRIMARY KEY IDENTITY(1, 1), Country nvarchar(30), City nvarchar(30))

SELECT * FROM UsersLocation

INSERT INTO UsersLocation(Country, City)
VALUES
('UK', 'London'),
('Germany', 'Berlin'),
('Japan', 'Tokyo'),
('Turkey', 'Ankara'),
('Turkey', 'Stambul'),
('Kazakhstan', 'Astana'),
('Belarus', 'Minsk'),
('Italy', 'Rome'),
('China', 'Beijing'),
('USA', 'New York'),
('USA', 'Washington'),
('Portugal', 'Lisbon'),
('Romania', 'Bucharest'),
('France', 'Paris'),
('France', 'Lion')

SELECT * FROM UsersLocation
