# Write your MySQL query statement below
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING sum(price) = (
    SELECT sum(price)
    FROM Sales
    GROUP BY seller_id
    ORDER BY sum(price) DESC LIMIT 1
)
