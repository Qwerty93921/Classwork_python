CREATE VIEW [Brazil Customers] as -- Скобки потому что ПРОБЕЛ в НАЗВАНИИ
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil'

-----------------------------------------------------------------------------

CREATE VIEW [Products above Average Price] as
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products)

-----------------------------------------------------------------------------

--DROP VIEW
-- для удаления

--COMMIT - сохранение базы данных(ctrl+s)
--ROLLBACK - вернуть назад(ctrl+z)

--BEGIN - начало транзакции

--транзакция - несколько скриптов

BEGIN
    UPDATE table_name SET field_1 = NULL WHERE id = 5
    DELETE FROM other_table WHERE id = 17
    SAVEPOINT point_name
    DELETE FROM test_table WHERE id = 75
    ROLLBACK TO SAVEPOINT point_name
COMMIT

LEN --Показывает количество символов в строке
LTRIM
PATINDEX
LEFT
RIGHT
CONCAT --Объединяет две строку в одну

--ROUND - округление
ROUND(1350.123, 2) --1350.12
ROUND(1350.123, -2) --1300(-2 значит до плавающей точки(десятых чисел) идет округление)

SELECT CONVERT(int, 'sql') --ошибка
TRY_CONVERT(int, '22') --22

CASE
if ...
ELSE
-------------------------------------------------------------------------------------
COALESCE

SELECT FirstName, LastName,
    COALESCE(Phone, Email, 'неопределено') AS Contacts
FROM Clients

--------------------------------------------------------------------------------------------
--Practice
--DT_PZ_09
--До 29 числа сдать дз

-- 1 task

SELECT * FROM Wards

SELECT Name, Places FROM Wards
WHERE DepartmentId = 5 AND Places > 5

-- 2 task

SELECT * FROM Departments
SELECT * from Wards
select * from DoctorsExaminations


SELECT DISTINCT d.Name
FROM Departments as d
JOIN Wards as w ON d.Id = w.DepartmentId
INNER JOIN DoctorsExaminations as de ON w.Id = de.WardId
WHERE de.Date >= DATEADD(WEEK, -1, GETDATE());

--Dateadd - манипуляция с датой
--WEEK, -1 - значит на НЕДЕЛЮ НАЗАД(-7 дней)
--GETDATE - текущая дата
-- - 7 дней ОТ ТЕКУЩЕЙ ДАТЫ

--3 task

select * from DoctorsExaminations
select * from Diseases

SELECT * FROM Diseases
WHERE Id NOT IN (SELECT DiseaseId FROM DoctorsExaminations)

-- 4 task
select * from DoctorsExaminations
select * from Diseases
select * from Doctors

select Name, Surname from Doctors
