# Write your MySQL query statement below
SELECT e.employee_id, b.team_size
FROM Employee as e
INNER JOIN
(SELECT team_id, COUNT(*) as team_size
FROM Employee 
GROUP BY team_id) b
ON e.team_id = b.team_id
