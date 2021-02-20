--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.0

-- Started on 2021-02-19 16:33:32

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16458)
-- Name: auth_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_users (
    id integer NOT NULL,
    code text NOT NULL
);


ALTER TABLE public.auth_users OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16470)
-- Name: creatures; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.creatures (
    sector_id integer NOT NULL,
    user_id integer NOT NULL,
    amount integer NOT NULL,
    type text NOT NULL
);


ALTER TABLE public.creatures OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16464)
-- Name: message; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.message (
    id integer NOT NULL,
    msg text NOT NULL,
    "time" text NOT NULL
);


ALTER TABLE public.message OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16489)
-- Name: profiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profiles (
    user_id integer NOT NULL,
    type text NOT NULL,
    color text NOT NULL
);


ALTER TABLE public.profiles OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16503)
-- Name: sectors_food; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sectors_food (
    id integer NOT NULL,
    food integer NOT NULL
);


ALTER TABLE public.sectors_food OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16501)
-- Name: sectors_food_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sectors_food_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sectors_food_id_seq OWNER TO postgres;

--
-- TOC entry 3037 (class 0 OID 0)
-- Dependencies: 208
-- Name: sectors_food_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sectors_food_id_seq OWNED BY public.sectors_food.id;


--
-- TOC entry 206 (class 1259 OID 16475)
-- Name: sectors_position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sectors_position (
    id integer NOT NULL,
    position_top integer NOT NULL,
    position_left integer NOT NULL
);


ALTER TABLE public.sectors_position OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16473)
-- Name: sectors_position_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sectors_position_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sectors_position_id_seq OWNER TO postgres;

--
-- TOC entry 3038 (class 0 OID 0)
-- Dependencies: 205
-- Name: sectors_position_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sectors_position_id_seq OWNED BY public.sectors_position.id;


--
-- TOC entry 201 (class 1259 OID 16452)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(30),
    login character varying(50),
    hpsw text,
    email character varying(50)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16450)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3039 (class 0 OID 0)
-- Dependencies: 200
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 2885 (class 2604 OID 16506)
-- Name: sectors_food id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sectors_food ALTER COLUMN id SET DEFAULT nextval('public.sectors_food_id_seq'::regclass);


--
-- TOC entry 2884 (class 2604 OID 16478)
-- Name: sectors_position id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sectors_position ALTER COLUMN id SET DEFAULT nextval('public.sectors_position_id_seq'::regclass);


--
-- TOC entry 2883 (class 2604 OID 16455)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3024 (class 0 OID 16458)
-- Dependencies: 202
-- Data for Name: auth_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_users (id, code) VALUES (2, '0398124657');
INSERT INTO public.auth_users (id, code) VALUES (1, '8052174396');
INSERT INTO public.auth_users (id, code) VALUES (3, '5470361829');


--
-- TOC entry 3026 (class 0 OID 16470)
-- Dependencies: 204
-- Data for Name: creatures; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.creatures (sector_id, user_id, amount, type) VALUES (1, 1, 1, 'травоядный');
INSERT INTO public.creatures (sector_id, user_id, amount, type) VALUES (1, 2, 1, 'хищник');


--
-- TOC entry 3025 (class 0 OID 16464)
-- Dependencies: 203
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3029 (class 0 OID 16489)
-- Dependencies: 207
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.profiles (user_id, type, color) VALUES (1, 'травоядный', 'синий');
INSERT INTO public.profiles (user_id, type, color) VALUES (2, 'хищник', 'красный');


--
-- TOC entry 3031 (class 0 OID 16503)
-- Dependencies: 209
-- Data for Name: sectors_food; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.sectors_food (id, food) VALUES (1, 1000);
INSERT INTO public.sectors_food (id, food) VALUES (2, 890);
INSERT INTO public.sectors_food (id, food) VALUES (3, 1200);
INSERT INTO public.sectors_food (id, food) VALUES (4, 500);
INSERT INTO public.sectors_food (id, food) VALUES (5, 8500);
INSERT INTO public.sectors_food (id, food) VALUES (6, 5990);
INSERT INTO public.sectors_food (id, food) VALUES (7, 4000);
INSERT INTO public.sectors_food (id, food) VALUES (8, 100);
INSERT INTO public.sectors_food (id, food) VALUES (9, 2500);


--
-- TOC entry 3028 (class 0 OID 16475)
-- Dependencies: 206
-- Data for Name: sectors_position; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (1, 1, 1);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (2, 1, 2);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (3, 1, 3);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (4, 2, 1);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (5, 2, 2);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (6, 2, 3);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (7, 3, 1);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (8, 3, 2);
INSERT INTO public.sectors_position (id, position_top, position_left) VALUES (9, 3, 3);


--
-- TOC entry 3023 (class 0 OID 16452)
-- Dependencies: 201
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, name, login, hpsw, email) VALUES (1, 'admin', 'admin', 'pbkdf2:sha256:150000$Xl7kq6Mm$3a80d49613f4c0c9ebce9fdbd4bf32dab9d8bc8a3de913a46bdf71b401e6592e', 'admin@ya.ru');
INSERT INTO public.users (id, name, login, hpsw, email) VALUES (2, 'cat', 'cat', 'pbkdf2:sha256:150000$uj4ph1ux$13e5fa34e3c13984be0fd258f517f1f1757e74aa871e8a8b4ad6d48bd13c0746', 'cat@ya.ru');
INSERT INTO public.users (id, name, login, hpsw, email) VALUES (3, 'lena', 'lena', 'pbkdf2:sha256:150000$uqNV4T2b$66080809bf7389cbb439624fea749f51b23a1bc4d11e7e2525156be1e0aecd38', 'lena@.ru');
INSERT INTO public.users (id, name, login, hpsw, email) VALUES (4, 'dog', 'dog', 'pbkdf2:sha256:150000$2NKmH13E$78e82a60376d303b21d66475b6bbb019f9ec6e47c026306a8c1c7519c257cd9e', 'dog');


--
-- TOC entry 3040 (class 0 OID 0)
-- Dependencies: 208
-- Name: sectors_food_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sectors_food_id_seq', 9, true);


--
-- TOC entry 3041 (class 0 OID 0)
-- Dependencies: 205
-- Name: sectors_position_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sectors_position_id_seq', 12, true);


--
-- TOC entry 3042 (class 0 OID 0)
-- Dependencies: 200
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- TOC entry 2891 (class 2606 OID 16508)
-- Name: sectors_food sectors_food_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sectors_food
    ADD CONSTRAINT sectors_food_pkey PRIMARY KEY (id);


--
-- TOC entry 2889 (class 2606 OID 16480)
-- Name: sectors_position sectors_position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sectors_position
    ADD CONSTRAINT sectors_position_pkey PRIMARY KEY (id);


--
-- TOC entry 2887 (class 2606 OID 16457)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


-- Completed on 2021-02-19 16:33:33

--
-- PostgreSQL database dump complete
--

