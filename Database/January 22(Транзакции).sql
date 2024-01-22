BEGIN TRANSACTION --Транзакция 1 началась
    INSERT INTO Customer VALUES(1, 'Code_1', 'David')
    INSERT INTO Customer VALUES(2, 'Code_2', 'John')

    BEGIN TRANSACTION --Транзакция 2 началась
        INSERT INTO Customer VALUES(3, 'Code_4', 'Pam')
        INSERT INTO Customer VALUES(4, 'Code_4', 'John_second')
    COMMIT TRANSACTION --Транзакция 2 завершилась

COMMIT TRANSACTION --Транзакция 1 завершилась
--ROLLBACK TRANSACTION
--ROLLBACK TRAN

-----------------------------------------------------------------------------

--Транзакция выполняет ВСЕ СРАЗУ либо АБСОЛЮТНО НИЧЕГО 

--COMMIT - сохранение(как ctrl + s)
--ROLLBACK - (откат)старые данные возвращает и не завершает транзакцию

--SELECT ... WHERE ... GROUP BY ... HAVING ...

--До 73 включительно вопросы на экзамен
