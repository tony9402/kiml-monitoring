--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.3

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
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."status" (
    uuid character varying NOT NULL,
    status character varying NOT NULL,
    run_name character varying NOT NULL,
    experiment_name character varying NOT NULL,
    experiment_id character varying NOT NULL,
    image character varying NOT NULL,
    instance_type character varying NOT NULL,
    create_time timestamp without time zone,
    start_time timestamp without time zone,
    end_time timestamp without time zone
);


ALTER TABLE public."status" OWNER TO postgres;

--
-- Name: COLUMN "status".status; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".uuid IS '작업 uuid';


--
-- Name: COLUMN "status".status; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".status IS '작업 상태';


--
-- Name: COLUMN "status".run_name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".run_name IS '실행 이름';


--
-- Name: COLUMN "status".experiment_name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".experiment_name IS '실험 이름';


--
-- Name: COLUMN "status".experiment_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".experiment_id IS '실험 id';


--
-- Name: COLUMN "status".image; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".image IS '실행 이미지';


--
-- Name: COLUMN "status".instance_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".instance_type IS 'GPU 인스턴스 타입';


--
-- Name: COLUMN "status".create_time; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".create_time IS '실험 제출 시각';


--
-- Name: COLUMN "status".start_time; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".start_time IS '실험 시작 시각';


--
-- Name: COLUMN "status".end_time; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public."status".end_time IS '실험 종료 시각';


ALTER TABLE ONLY public."status"
    ADD CONSTRAINT status_pkey PRIMARY KEY (uuid);


--
-- PostgreSQL database dump complete
--

