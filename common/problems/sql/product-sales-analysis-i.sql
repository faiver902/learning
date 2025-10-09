# Write your MySQL query statement below
select product_name, year, price from product join sales on sales.product_id = product.product_id;
