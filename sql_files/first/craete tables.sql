 create table if  not exists public.user (
    id int PRIMARY KEY,
    name varchar
);
create table if not exists public.profile (
    user_id int,
    hobbes varchar,
    foreign key (user_id) references public.user(id)
);