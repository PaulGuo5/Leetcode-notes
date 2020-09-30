# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) as unit
FROM Products as p
JOIN Orders as o
ON p.product_id = o.product_id
WHERE o.order_date between '2020-02-01' and '2020-02-31'
GROUP BY p.product_id
HAVING unit >= 100

