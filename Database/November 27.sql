-- SSMS
-- SQL Server Management Studio

select * from Customers

select * from Orders

select c.CustomerID, c.CompanyName,
c.ContactName, ord.OrderDate,
ord.ShipCity
from Customers as c
join Orders as ord on
c.CustomerID = ord.CustomerID
where ord.ShipCity = 'Madrid'
order by c.CustomerID

-- клиенты которые сделали заказ

--Shipcity
--Клиенты которые делали заказ в Мадрид

select * from Orders
select * from Employees

--Вывести информацию по работнику
--emp.LastName, firstname, title

select emp.EmployeeID, emp.LastName, emp.FirstName, emp.BirthDate, emp.HireDate, emp.Address, emp.City
from Employees as emp

select c.CustomerID, c.CompanyName, c.ContactName,
ord.OrderDate, ord.Shipcity,
emp.LastName, emp.FirstName, emp.Title
from Customers as c
join Orders as ord on c.CustomerID = ord.CustomerID
join Employees as emp on emp.EmployeeID = ord.EmployeeID

----------------------------------------------------------
select * from Categories
select * from Employees

select COUNT(*)
from Categories
-- Count показывает сколько СТРОК в таблице ВЕРТИКАЛЬНО
-- Агрегированные функции

-- Агрегатная функция выполняет вычисление над набором значений и 
-- возвращает одно значение. В табличной модели данных это значит, что функция берет ноль, 
-- одну или несколько строк для какой-то колонки и возвращает единственное значение.
------------------------------------------------------------------

select COUNT(*)
from Employees

select COUNT(emp.TitleofCourtesy)
from Employees as emp

select count (distinct emp.TitleofCourtesy) as cnt_2
from Employees as emp

---------------------------------------------------------------
select * from Employees as emp

------------------------------------------------------------------

select avg(p.UnitPrice) as 'avg product price'
from Products as p
--------------------------------------------------------------------------------

select sum(p.Unitprice) as 'total product price'
from products as p

--------------------------------------------------------------------------------
select min(p.Unitprice)
as 'min product price'
from Products as p

--------------------------------------------------------------------------------
select max(p.Unitprice)
as 'max product price'
from Products as p

--------------------------------------------------------------------------------
select
max(p.Unitprice) as 'max product price',
min(p.Unitprice) as 'min product price'
from Products as p

--------------------------------------------------------------------------------
select * from Products as p

select p.CategoryID,
count(p.CategoryID) as cnt_category
from Products as p
group by p.CategoryID

--------------------------------------------------------------------------------
select * from Products as p

select sum(p.UnitsInStock) as 'amount of products'
from products as p

--Количество продуктов на складе через sum()
--------------------------------------------------------------------------------

select 
p.CategoryID,
c.CategoryName,
count(p.CategoryID) as cnt_category,
avg(p.UnitPrice) as avg_price,
sum(p.UnitsInStock) as sum_stock 
from Products p
join Categories c
on c.CategoryID = p.CategoryID
group by p.CategoryID, c.CategoryName;

--------------------------------------------------------------------------------
-- HAVING - это WHERE после ГРУППИРОВКИ(group by)

-- SELECT columnName1, columnName2, ...
-- FROM tableName
-- [WHERE condition]
-- [GROUP BY columnName1, columnName2, ...]
-- HAVING condition
-- [ORDER BY columnName1 ASC | DESC, ...];

--------------------------------------------------------------------------------

-- select 
-- p.CategoryID,
-- c.CategoryName,
-- count(p.CategoryID) as cnt_category,
-- avg(p.UnitPrice) as avg_price,
-- sum(p.UnitsInStock) as sum_stock 
-- from Products p
-- join Categories c
-- on c.CategoryID = p.CategoryID
-- where p.ProductName like 'C%'
-- group by p.CategoryID, c.CategoryName
-- having count(p.CategoryID) > 1;
