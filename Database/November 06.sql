drop table products;
-- drop - удалить таблицу

create table products (
product_no int primary key,
name nvarchar(50),
price money
)

-- primary key - значит что значение должно быть уникальным и не повторяться
-- nvachar(число) - значит ФОРМАТ ТЕКСТА, ЧИСЛО В СКОБКАХ значит количество СИМВОЛОВ НЕ БОЛЕЕ чем в скобках

-- нужно выделять N количество строк и нажимать кнопку "выполнить" чтобы выполнить ТОЛЬКО ВЫДЕЛЕННОЕ, а не весь файл
-- все название ТОЛЬКО В ОДИНАРНЫХ КАВЫЧКАХ
-- insert - добавить в ТАБЛИЦУ что-то

create table orders(
order_id int primary key,
product_no int references products (product_no),
quantity int
)

insert into products(product_no, name, price)
values(1, 'laptop', 10000)

select * from products;

insert into products(product_no, name, price)
values(2, 'phone', 20000)

insert into products(product_no, name)
values(3, 'tv')

select * from orders;

insert into orders(order_id, product_no, quantity)
values(1, 1, 10)

insert into orders(order_id, product_no, quantity)
values(2, 2, 5)


create table users (
id int,
name varchar(200),
age int,
email varchar(200)
)

drop table users;

select * from users;

insert into users(id, name, age, email)
values(1, 'qwe', 90, 'qwe@mail.com')
