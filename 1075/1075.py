# Write your MySQL query statement below
SELECT p.project_id AS project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project as p, Employee as e
WHERE p.employee_id = e.employee_id
GROUP BY project_id
