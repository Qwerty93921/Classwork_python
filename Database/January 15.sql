--task 7

select * from Interns

select * from Doctors

select d.Surname
from Doctors as d
join Interns i on d.Id = i.DoctorId

select Salary from Doctors

select d.Surname
from Doctors as d
join Interns i on d.Id = i.DoctorId
where d.Salary > any
(
select dd.Salary from Doctors as dd
where dd.Id not in (select i.DoctorId from Interns)
)


--select d.Surnamefrom Doctors d
--join Interns i on d.Id = i.DoctorIdwhere d.Salary > any 
--(select dd.Salary from Doctors dd
--where dd.Id not in (select i.DoctorId from Interns i))

--task 8
SELECT w.Name
FROM Wards as w
WHERE w.Places > ALL
(
	SELECT Places FROM Wards WHERE DepartmentId IN
		(SELECT Id FROM Departments WHERE Building = 2)
)
