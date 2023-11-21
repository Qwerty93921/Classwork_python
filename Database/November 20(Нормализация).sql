-- https://www.w3schools.com/sql/sql_foreignkey.asp
-- https://www.w3schools.com/sql/sql_join_inner.asp

-- PG admin 4 V7
-- SS MS
-- Microsoft SQL Server Management Studio

-- Нормализация - процесс удаления избыточных данных
-- CONSTRAINT - ограничения(Not null, unique, foreign key, primary key)

-- ненормальная форма - НУЛЕВАЯ форма
-- 2NF - вторая нормальная форма(нужна сначала первая нормальная форма)

-- ----------------------------------------------------------------------------

select Orders.OrderI, Customers.CustomerName, Orders.OrderData
from Customers
INNER JOIN Orders
ON Orders.CustomerID=Customers.CustomerID;

-- Соединение двух таблиц ORDERS и CUSTOMERS,после ТОЧКИ НАЗВАНИЕ СТОЛБЦА
-- INNER JOIN Orders - значит СОЕДИНИТЬ вторую таблицу с первой
-- ON - ключевое слово для выполнения команды

-- ----------------------------------------------------------------------------

-- если писать ПРОСТО JOIN это по умолчанию = INNER JOIN
-- INNER JOIN - значит СОЕДИНИТЬ вторую таблицу с первой
-- LEFT JOIN - выводит ВСЕ с ПЕРВОЙ таблицы и ОБЩЕЕ со второй
-- RIGHT JOIN - выводит ВСЕ со ВТОРОЙ таблицы и ОБЩЕЕ с ПЕРВОЙ
-- FULL JOIN - выводит полностью первую таблицу и полностью вторую

-- ----------------------------------------------------------------------------

-- Если писать LEFT join - будет 213 результат
-- Если писать INNER join - будет 196 результат
-- Это потому что в LEFT выводится ВСЕ ПОДРЯД, даже где клиент НЕ СДЕЛАЛ ЗАКАЗ(null)
-- В INNER join - он null выводить не будет

-- ----------------------------------------------------------------------------

-- ПСЕВДОНИМЫ
-- Можно без AS

SELECT CustomerID as ID
FROM Customers;
-- или
-- SELECT CustomerID ID

-- ----------------------------------------------------------------------------

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;

-- Даем псевдоним(ник) на таблицу Customers как "C", Orders как "o"

-- ----------------------------------------------------------------------------

-- SELECT * FROM users;

-- SELECT * from users
-- WHERE age < 30;

-- SELECT * from users
-- WHERE name LIKE 'A%'
