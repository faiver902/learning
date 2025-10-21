CREATE INDEX IF NOT EXISTS profile_hobbes_idx  on public.user(name);
CREATE INDEX IF NOT EXISTS user_name_idx on public.profile(hobbes);
CREATE INDEX IF NOT EXISTS user_name_num_idx
  ON public."user" ( (substring(name FROM 6)::int) );

ANALYZE public."user";
