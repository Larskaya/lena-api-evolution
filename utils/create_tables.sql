CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(30),
    login CHARACTER VARYING(50),
    hpsw  TEXT NOT NULL,
    email CHARACTER VARYING(50)
);

CREATE TABLE auth_users (
    id INTEGER NOT NULL,
    code CHARACTER VARYING(20)
);

CREATE TABLE messages (
    id INTEGER NOT NULL,
    msg TEXT NOT NULL,
    time CHARACTER VARYING(30)
);

CREATE TABLE creatures (
    sector_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    type INTEGER NOT NULL
);


CREATE TABLE sectors (
    id SERIAL PRIMARY KEY,
    position_top INTEGER NOT NULL,
    position_left INTEGER NOT NULL,
    food INTEGER NOT NULL,
    type INTEGER NOT NULL
);

CREATE TABLE profiles (
    user_id  INTEGER NOT NULL,
    color CHARACTER VARYING(20),
    type INTEGER NOT NULL
)
