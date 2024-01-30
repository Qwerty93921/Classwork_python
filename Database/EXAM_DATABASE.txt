--1

select * from Products

--2

select * from Orders

select OrderID from Orders
WHERE ShipCountry Like 'U%'

--3

select * from Products

select AVG(UnitPrice)
FROM Products

--4

select * from Orders
select * from Customers

select COUNT(OrderID)
FROM Orders
WHERE CustomerID = CustomerID
	
--5

select * from Orders

select CustomerID from Orders
WHERE ShipCountry = 'USA'

--6

select * from Products
select * from Categories
select * from Suppliers

------------------------------------------------------------------------------------------

select Products.ProductName, Suppliers.CompanyName
FROM Products
INNER JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID

select Products.ProductName, Categories.CategoryName
FROM Products
INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID


--7

Select * from Customers
Select * from Suppliers

select  Country
FROM Customers
UNION
select  Country
FROM Suppliers

--8

select * from Orders
select * from Products

CREATE VIEW OrderTotal AS
SELECT Orders.CustomerID, Products.UnitPrice
SUM(Orders)

--9

select * from  Products

INSERT INTO Products(ProductName, QuantityPerUnit, UnitPrice)
VALUES('New_product', '5kg', 40)

--10

select * from Products
select * from Categories

UPDATE Products
SET UnitPrice = UnitPrice * 1.1
WHERE CategoryID = 1

--11

select * from Products
select * from [Order Details]

delete from Products
WHERE NOT EXISTS(
	SELECT 1
	FROM [Order Details]
	WHERE [Order Details].ProductID = Products.ProductID
)

--12

--JOIN есть 4 видов
--JOIN - он используется для объединения строк из 2 или больше таблиц на основе связанной между ними колонки

--INNER JOIN - возвращает только совпадающие значения с двух таблиц
--LEFT JOIN - возвращает все значения из первой таблицы, но из второй возвращает только совпадающие значения
--RIGHT JOIN - возвращает все значения из второй таблицы, но из первой возвращает только совпадающие значения
--FULL JOIN - возвращает все записи из двух таблиц при наличии совпадений, если их нет, может писать NULL в значениях


--Синтаксис
--select Products.ProductName, Suppliers.CompanyName
--FROM Products
--INNER JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
