--https://metanit.com/sql/sqlserver/11.2.php

USE productsdb;
GO --GO можно не писать и ничего не поменяется
CREATE PROCEDURE AddProductWithOptionalCount
    @name NVARCHAR(20),
    @manufacturer NVARCHAR(20),
    @price MONEY,
    @count INT = 1
AS
INSERT INTO Products(ProductName, Manufacturer, ProductCount, Price) 
VALUES(@name, @manufacturer, @count, @price)

--Процедура - это как ФУНКЦИЯ, но она МОЖЕТ НИЧЕГО НЕ ВОЗВРАЩАТЬ(ФУНКЦИЯ вернет NULL или результат)

-----------------------------------------------------------------------------

DECLARE @prodName NVARCHAR(20), @company NVARCHAR(20), @price MONEY
SET @prodName = 'Redmi Note 5A'
SET @company = 'Xiaomi'
SET @price = 22000
 
EXEC AddProductWithOptionalCount @prodName, @company, @price
--EXEC или EXECUTE - это выполнить транзакцию(название)


SELECT * FROM Products

--Declare - СОЗДАНИЕ ПЕРЕМЕННОЙ
--SET - ВЫДАЧА ЗНАЧЕНИЙ переменной

-----------------------------------------------------------------------------

USE productsdb;
 
DECLARE @prodName NVARCHAR(20), @company NVARCHAR(20);
SET @prodName = 'Honor 9'
SET @company = 'Huawei'
 
EXEC AddProduct @name = @prodName, 
                @manufacturer=@company,
                @count = 3, 
                @price = 18000

-----------------------------------------------------------------------------

--PRINT - работает ТОЛЬКО С STR форматом(VARCHAR, NVARCHAR)

-----------------------------------------------------------------------------

USE productsdb
DECLARE @minPrice MONEY, @maxPrice MONEY

EXEC GetPriceStats @minPrice OUTPUTm @maxPrice OUTPUTm

PRINT 'Минимальная цена' + CONVERT(VARCHAR, @minPrice)
PRINT 'Максимальная цена' + CONVERT(VARCHAR, @maxPrice)

-- ... OUTPUT - это RETURN для ПРОЦЕДУР
