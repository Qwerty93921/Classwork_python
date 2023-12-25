select * from Customers
select * from Products
---------------------------------------------------------------------------------------

select Suppliers.SupplierID, Products.ProductName, Suppliers.ContactName
from Suppliers
INNER JOIN Products ON Suppliers.SupplierID = Products.ProductID

order by SupplierID desc
--desc - обратный порядок чисел
--HAVING как WHERE, с функциями АГРЕГИРОВАНИЯ ПОСЛЕ GROUP BY

---------------------------------------------------------------------------------------

select * from Suppliers;
select * from Products;

-- нужно создать view где будет информация по поставщику
-- у которого больше всего продуктов
-- Suppliers.CompanyName, ContactName, ContactTitle

select max(SupplProducts_Count) as max_cnt from (
 select count(1) as SupplProducts_Count
 from Products p
 group by p.SupplierID
) as max_supl_tbl;


select max(SupplProducts_Count) as max_cnt
from (
 select 
 count(1) as SupplProducts_Count
 from Products p
 group by p.SupplierID
) as max_cnt_supl_tbl;


select 
p.SupplierID
from Products p
group by p.SupplierID
having count(1) = (
 select max(SupplProducts_Count) as max_cnt
from (
 select 
 count(1) as SupplProducts_Count
 from Products p
 group by p.SupplierID
 ) as max_cnt_supl_tbl
);

alter view SupplierTopProducts as
select sp.CompanyName as TestColumn, sp.ContactName, sp.ContactTitle
from Suppliers sp
where sp.SupplierID in
 (
 select 
 p.SupplierID
 --count(1)
 from Products p
 group by p.SupplierID
 having count(1) = (
  select max(SupplProducts_Count) as max_cnt
 from (
   select 
   count(1) as SupplProducts_Count
   --p.SupplierID
   from Products p
   group by p.SupplierID

  ) as max_cnt_supl_tbl
   )
 );


select * from SupplierTopProducts;



select sp.CompanyName, sp.ContactName, sp.ContactTitle
from Suppliers sp
where sp.SupplierID in
 (
 select 
 p.SupplierID
 --count(1)
 from Products p
 group by p.SupplierID
 having count(1) = 5
 );


select p.SupplierID, count(1) as SupplProducst_Count
from Products p
group by p.SupplierID
order by count(1) desc;


select * from Products pp
where pp.SupplierID in 
 (select TOP 1 p.SupplierID
 from Products p
 group by p.SupplierID
 order by count(1) desc);


select sp.CompanyName, sp.ContactName, sp.ContactTitle
from Suppliers sp
where sp.SupplierID in 
 (select TOP 1 p.SupplierID
 from Products p
 group by p.SupplierID
 order by count(1) desc);

----------------------------------------------------------------------------------------------------------------

--SELECT * FROM ##OrderDetails
--Временная таблица которая работает только при СОЕДИНЕНИИ с СЕРВЕРОМ и ИСЧЕЗАЕТ при закрытии

----------------------------------------------------------------------------------------------------------------

--CREATE VIEW table2
--временная таблица которая СОХРАНЯЕТСЯ В ПАМЯТИ и показывает актуальные данные

----------------------------------------------------------------------------------------------------------------

with ProductsSuppliersCount as (
 select 
 count(1) as SupplProducts_Count,
 p.SupplierID
 from Products p
 group by p.SupplierID
)
select * from ProductsSuppliersCount ps
where ps.SupplProducts_Count = 5;

----------------------------------------------------------------------------------------------------------------

SELECT * FROM ##OrderDetails
--ВРЕМЕННАЯ ПЕРЕМЕННАЯ которая УДАЛЯЕТСЯ при закрытии

with ProductsSuppliersCount as (
	select 
	count(1) as SupplProducts_Count,
	p.SupplierID
	from Products p
	group by p.SupplierID
)

select * from ProductsSuppliersCount as ps
join Categories as c
on ps.CategoryID = c.CategoryID

select * from [Orders Qry]
