# Write your MySQL query statement below
select p.FirstName as FirstName, p.LastName as LastName, a.City as City, a.State as State
from Person as p
left join Address as a
on p.PersonId = a.PersonId
