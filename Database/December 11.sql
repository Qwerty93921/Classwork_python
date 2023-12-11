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
