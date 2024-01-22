--https://www.sqlshack.com/learn-sql-user-defined-functions/

CREATE FUNCTION east_or_west (
	@long DECIMAL(9,6) --9 чисел до запятой и 6 после запятой
)
RETURNS CHAR(4) AS --returnS (тип данных после этого, А НЕ РЕЗУЛЬТАТ)
BEGIN
	DECLARE @return_value CHAR(4);
	SET @return_value = 'same';
    IF (@long > 0.00) SET @return_value = 'east';
    IF (@long < 0.00) SET @return_value = 'west';
 
    RETURN @return_value --return(БЕЗ S) - конечный результат
END;

SELECT *, dbo.east_or_west
...


SELECT *
FROM east_or_west(0.00)
