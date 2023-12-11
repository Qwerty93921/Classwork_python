select * from Products

--найти категорию продукта с макс ценой
--max_price = 263,50

select max(p.UnitPrice) as max_price
from Products as p;

--CategoryID = 1
select CategoryID from Products
where UnitPrice =
	(select max(UnitPrice)
		from Products);

select c.CategoryName, c.Description
from Categories as c
where c.CategoryID = 1;

select c.CategoryName, c.Description
from Categories as c
where c.CategoryID IN --(1, 5)
(
	select CategoryID 
	from Products
		where UnitPrice =
			(select max(UnitPrice) from Products)
)

--Добавить новый продукт с максимальной ценой в таблицу Products

insert into Products(ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsOnOrder, ReorderLevel, Discontinued)
values(
'Bread Pit',
(select s.SupplierID from Suppliers as s where s.CompanyName = 'Tokyo Traders'),
(select c.CategoryID from Categories as c where c.CategoryName = 'Grains/Cereals'),
10,
263.50,
5,
0,
0
);

--------------------------------------------------------------------------------

--Practice 6

select * from Departments

--1 задание

--Вывести названия отделений, что находятся в том же 
--корпусе, что и отделение “Cardiology”

select Building from Departments
where Name = 'Cardiology'

Select Name
from Departments
where Building = 1

--2 задание

--Вывести названия отделений, что находятся в том же 
--корпусе, что и отделения “Gastroenterology” и “General 
--Surgery”.
select * from Departments
where Name = 'Gastroenterology' or Name = 'General Surgery'

--3 задание

--Вывести название отделения, которое получило меньше 
--всего пожертвований

------------------------------------------------------------------------------
select * from Donations

select DepartmentId from Donations as d
where Amount = 
(select MIN(Amount) from Donations)
-----------------------------------------------------------------------------

SELECT d.Name --TOP 1 d.Name
FROM Departments as d
JOIN Donations as don ON d.Id = don.DepartmentId
GROUP BY d.Id, d.Name
ORDER BY SUM(don.Amount) ASC;

--4 задание

--Вывести фамилии врачей, ставка которых больше, чем 
--у врача “Thomas Gerada”.
select * from Doctors

SELECT Surname FROM Doctors
WHERE Salary > (SELECT Salary FROM Doctors WHERE Name = 'Thomas Gerada');
