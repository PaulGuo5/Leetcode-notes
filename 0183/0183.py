# Write your MySQL query statement below
# SELECT Name as Customers
# FROM Customers
# WHERE Id not in
# (
#     SELECT CustomerId from Orders
# )
SELECT Name as Customers
FROM Customers as c
LEFT JOIN Orders as o
ON c.Id = o.CustomerId
WHERE o.CustomerId is null
