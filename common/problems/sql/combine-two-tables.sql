# Write your MySQL query statement below
select p1.firstName, p1.lastName, a1.city, a1.state from person as p1
left join address as a1 using(personId);