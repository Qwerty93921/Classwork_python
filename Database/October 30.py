# СУБД - система управления базой данных
# PostgreSQL - structured query language
# Реляционная база данных - relation
# 
# Postgre, oracle, microsoft sql server(MS SQL), MS Access, MySQL, SQLite
# 
# W3School SQL - в google вводить
# https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
# 
# SELECT * from CUSTOMERS - все подряд выводит

# SELECT CustomerName, Address 
# FROM Customers
# выводит только CustomerName и Address

# SELECT distinct Country FROM Customers
# Выводит УНИКАЛЬНЫЕ названия(не повторяет один и тот же результат)
# DISTINCT

# SELECT * FROM Customers
# WHERE Country = "Mexico"
# Выводит ВСЕ данные где страна Мексика
# * значит ВСЕ ПОДРЯД

# SELECT CustomerName FROM Customers
# WHERE Country = "Mexico"
# Выводит имена клиентов из Мексики

# SELECT * FROM Customers
# WHERE CustomerName LIKE "a%"
# Выводит только имена которые НАЧИНАЮТСЯ на А
# "a%" - значит что НАЧИНАЕТСЯ на "a" и потом идет что угодно
# LIKE - фильтрует что-то

# SELECT * FROM Employees
# WHERE LastName LIKE "%g"
# Выводит фамилии которые ЗАКАНЧИВАЮТСЯ на "g"

# LIKE от "=" отличается тем что в "=" нужно писать СТОПРОЦЕНТНО ВЕРНУЮ ИНФОРМАЦИЮ
# в LIKE можно писать паттерны(заканчивается или начинается слово на что-то и искать по этому признаку)

# SELECT * FROM Customers
# WHERE city = "Berlin" or Country = "Canada"

# SELECT * FROM Suppliers
# WHERE SupplierName LIKE "%o%"
# or City = "Tokyo" and Country = "Japan"

# В имени поставщика есть буква "O"
# и город Токио и Страна Япония

# SELECT * FROM Customers
# WHERE Country != "Mexico"

# НЕ ВЫВОДИТ страну Mexico


# SELECT * FROM Customers
# WHERE Country = "Germany" or country = "France" or country = "UK" or country = "Mexico"

# WHERE Country IN ("Germany", "France", "UK", "Mexico")
# Одинаковый результат