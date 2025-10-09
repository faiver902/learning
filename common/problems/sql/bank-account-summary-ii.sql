select u.name, sum(t.amount) as balance from users as u join transactions as t using(account) group by u.name having balance>10000;
