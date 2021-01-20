CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(30),
    login CHARACTER VARYING(50),
    hpsw CHARACTER VARYING(70),
    email CHARACTER VARYING(50)
);

CREATE TABLE auth_users (
    id INTEGER NOT NULL,
    code TEXT NOT NULL
);

CREATE TABLE messages (
    id INTEGER NOT NULL,
    msg TEXT NOT NULL,
    time TEXT NOT NULL
);

CREATE TABLE creatures (
    sector_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    amount INTEGER NOT NULL
);

CREATE TABLE sectors_position (
    id SERIAL PRIMARY KEY,
    position_top INTEGER NOT NULL,
    position_left INTEGER NOT NULL
);

CREATE TABLE sectors_food (
    id INTEGER NOT NULL,
    food INTEGER NOT NULL
);

CREATE TABLE profiles (
    id  INTEGER NOT NULL,
    type CHARACTER VARYING(20),
    color CHARACTER VARYING(20)
)
