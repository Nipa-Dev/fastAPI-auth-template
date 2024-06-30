CREATE TABLE IF NOT EXISTS public.users (
    user_id text NOT NULL,
    username text UNIQUE,
    hashed_password text NOT NULL,
    key_salt text,
    fullname text NOT NULL,
    email text UNIQUE,
    scopes text array NOT NULL DEFAULT ARRAY['users:default'],
    is_banned boolean NOT NULL DEFAULT false,
    is_admin boolean NOT NULL DEFAULT false,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);
