--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: experience; Type: TABLE; Schema: public; Owner: john
--

CREATE TABLE public.experience (
    id integer NOT NULL,
    company character varying,
    designation character varying,
    city character varying,
    start_date date,
    end_date date,
    type character varying,
    role_description character varying,
    user_id integer
);


ALTER TABLE public.experience OWNER TO john;

--
-- Name: experience_id_seq; Type: SEQUENCE; Schema: public; Owner: john
--

CREATE SEQUENCE public.experience_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.experience_id_seq OWNER TO john;

--
-- Name: experience_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: john
--

ALTER SEQUENCE public.experience_id_seq OWNED BY public.experience.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: john
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    name character varying,
    city character varying,
    primary_email character varying,
    secondary_email character varying,
    primary_phone integer,
    secondary_phone integer,
    date_of_birth date,
    full_address character varying
);


ALTER TABLE public."user" OWNER TO john;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: john
--

CREATE SEQUENCE public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO john;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: john
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: john
--

ALTER TABLE ONLY public.experience ALTER COLUMN id SET DEFAULT nextval('public.experience_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: john
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: experience; Type: TABLE DATA; Schema: public; Owner: john
--

COPY public.experience (id, company, designation, city, start_date, end_date, type, role_description, user_id) FROM stdin;
1	TCS	System Engineer	Mumbai	2000-01-01	2007-01-30	Full-Time	Worked on Software Development	1
2	Infosys	System Engineer	Bangalore	2007-02-01	2024-01-30	Full-Time	Worked on Software Development	1
3	Infosys	System Engineer	Bangalore	2007-02-01	2013-01-30	Full-Time	Worked on Software Development	3
4	Infosys	System Engineer	New Delhi	2013-02-01	2015-01-30	Full-Time	Worked on Software Development	3
5	Infosys	System Engineer	New Delhi	2015-02-01	2018-01-30	Full-Time	Worked on Software Development	3
\.


--
-- Name: experience_id_seq; Type: SEQUENCE SET; Schema: public; Owner: john
--

SELECT pg_catalog.setval('public.experience_id_seq', 5, true);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: john
--

COPY public."user" (id, name, city, primary_email, secondary_email, primary_phone, secondary_phone, date_of_birth, full_address) FROM stdin;
1	Bhavesh	Mumbai	bhavesh@example.com	\N	123456789	12345678	1996-10-11	123 ABC Nagar, Navi Mumbai
3	Anand	Mumbai	anand@example.com	\N	123456780	12345678	1996-10-19	234 ABC Nagar, Navi Mumbai
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: john
--

SELECT pg_catalog.setval('public.user_id_seq', 3, true);


--
-- Name: experience_pkey; Type: CONSTRAINT; Schema: public; Owner: john
--

ALTER TABLE ONLY public.experience
    ADD CONSTRAINT experience_pkey PRIMARY KEY (id);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: public; Owner: john
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user_primary_email_key; Type: CONSTRAINT; Schema: public; Owner: john
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_primary_email_key UNIQUE (primary_email);


--
-- Name: user_primary_phone_key; Type: CONSTRAINT; Schema: public; Owner: john
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_primary_phone_key UNIQUE (primary_phone);


--
-- Name: experience_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: john
--

ALTER TABLE ONLY public.experience
    ADD CONSTRAINT experience_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

