# Write your MySQL query statement below
select d.name as Department, e.Name as Employee, Salary
from Employee as e, Department as d
where e.DepartmentId = d.Id
and Salary in (select max(e2.salary) from Employee as e2 where d.Id = e2.DepartmentId group by e2.DepartmentId)
