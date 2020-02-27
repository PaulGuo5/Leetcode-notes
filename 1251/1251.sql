# Write your MySQL query statement below
SELECT p.product_id, round(sum(u.units*p.price)/sum(u.units), 2) as average_price
FROM Prices as p
RIGHT JOIN UnitsSold as u
ON p.product_id = u.product_id
WHERE u.purchase_date between p.start_date and end_date
group by p.product_id
