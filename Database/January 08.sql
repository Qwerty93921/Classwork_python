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
