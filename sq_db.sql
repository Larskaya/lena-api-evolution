

CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text not null,
    login text not null,
    psw text not null,
    email text not null
);

CREATE TABLE IF NOT EXISTS auth_users (
    id integer not null,
    code text not null
);

CREATE TABLE IF NOT EXISTS messages (
    user_id integer not null,
    message text not null,
    time datetime NOT NULL
)



