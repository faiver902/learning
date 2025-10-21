truncate public.user cascade;

INSERT INTO public."user" (id, name)
SELECT i, 'user_' || i
FROM generate_series(1, 100000) AS s(i);

-- 1000 профилей
INSERT INTO public.profile (user_id, hobbes)
SELECT i, 'hobbie_' || i
FROM generate_series(1, 100000) AS s(i);
ANALYZE profile;
ANALYZE public.user;