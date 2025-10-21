ANALYZE public.profile;
ANALYZE public.user;

explain (analyse, buffers) select * from public.user as u
left join public.profile as p
on p.user_id = u.id
WHERE CAST(substring(name FROM 6) AS int) < 4;