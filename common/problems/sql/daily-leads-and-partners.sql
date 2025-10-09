# Write your MySQL query statement below
select date_id, make_name, count(distinct lead_id)as unique_leads , count(distinct partner_id) as unique_partners
from DailySales
group by date_id, make_name;

SELECT product_id, 'store1' as store, store1 AS price FROM products as p1
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' as store, store2 AS price FROM products as p2
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' as store, store3 AS price FROM products as p3
WHERE store3 IS NOT NULL;
