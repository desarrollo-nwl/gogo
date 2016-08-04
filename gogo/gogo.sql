--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.5
-- Dumped by pg_dump version 9.5.3

-- Started on 2016-06-14 09:17:53 COT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12723)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 3397 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 16395)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO suidi;

--
-- TOC entry 174 (class 1259 OID 16398)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO suidi;

--
-- TOC entry 3399 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- TOC entry 175 (class 1259 OID 16400)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO suidi;

--
-- TOC entry 176 (class 1259 OID 16403)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO suidi;

--
-- TOC entry 3402 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- TOC entry 177 (class 1259 OID 16405)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO suidi;

--
-- TOC entry 178 (class 1259 OID 16408)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO suidi;

--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- TOC entry 179 (class 1259 OID 16410)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(300) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO suidi;

--
-- TOC entry 180 (class 1259 OID 16416)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO suidi;

--
-- TOC entry 181 (class 1259 OID 16419)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO suidi;

--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- TOC entry 182 (class 1259 OID 16421)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO suidi;

--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- TOC entry 183 (class 1259 OID 16423)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO suidi;

--
-- TOC entry 184 (class 1259 OID 16426)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO suidi;

--
-- TOC entry 3414 (class 0 OID 0)
-- Dependencies: 184
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- TOC entry 227 (class 1259 OID 24355)
-- Name: colaboradores_360_colaboradores; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_360_colaboradores (
    id integer NOT NULL,
    apellido character varying(45) NOT NULL,
    descripcion character varying(255),
    email character varying(254) NOT NULL,
    enviados smallint NOT NULL,
    estado boolean NOT NULL,
    externo boolean NOT NULL,
    genero character varying(10),
    key character varying(64) NOT NULL,
    key_old character varying(64) NOT NULL,
    nombre character varying(45) NOT NULL,
    pre_aresponder smallint NOT NULL,
    pre_respuestas smallint NOT NULL,
    tot_avance smallint NOT NULL,
    can_instrumentos smallint NOT NULL,
    propension double precision NOT NULL,
    proyecto_id integer NOT NULL,
    puntaje double precision NOT NULL,
    reenviados smallint NOT NULL,
    respuestas smallint NOT NULL,
    CONSTRAINT colaboradores_360_colaboradores_can_instrumentos_check CHECK ((can_instrumentos >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_enviados_check CHECK ((enviados >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_pre_aresponder_check CHECK ((pre_aresponder >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_pre_respuestas_check CHECK ((pre_respuestas >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_reenviados_check CHECK ((reenviados >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_respuestas_check CHECK ((respuestas >= 0)),
    CONSTRAINT colaboradores_360_colaboradores_tot_avance_check CHECK ((tot_avance >= 0))
);


ALTER TABLE colaboradores_360_colaboradores OWNER TO suidi;

--
-- TOC entry 226 (class 1259 OID 24353)
-- Name: colaboradores_360_colaboradores_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE colaboradores_360_colaboradores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE colaboradores_360_colaboradores_id_seq OWNER TO suidi;

--
-- TOC entry 3417 (class 0 OID 0)
-- Dependencies: 226
-- Name: colaboradores_360_colaboradores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE colaboradores_360_colaboradores_id_seq OWNED BY colaboradores_360_colaboradores.id;


--
-- TOC entry 228 (class 1259 OID 24371)
-- Name: colaboradores_360_datos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_360_datos (
    id_id integer NOT NULL,
    area character varying(200),
    cargo character varying(200),
    fec_ingreso date,
    fec_nacimiento date,
    niv_academico character varying(50),
    opcional1 character varying(100),
    opcional2 character varying(100),
    opcional3 character varying(100),
    opcional4 character varying(100),
    opcional5 character varying(100),
    ciudad character varying(100),
    profesion character varying(200),
    regional character varying(200)
);


ALTER TABLE colaboradores_360_datos OWNER TO suidi;

--
-- TOC entry 229 (class 1259 OID 24379)
-- Name: colaboradores_360_metricas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_360_metricas (
    id_id integer NOT NULL,
    propension text NOT NULL,
    ord_instrumentos text NOT NULL,
    ins_actual integer NOT NULL,
    CONSTRAINT colaboradores_360_metricas_ins_actual_check CHECK ((ins_actual >= 0))
);


ALTER TABLE colaboradores_360_metricas OWNER TO suidi;

--
-- TOC entry 231 (class 1259 OID 24390)
-- Name: colaboradores_360_roles; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_360_roles (
    id integer NOT NULL,
    nombre character varying(128) NOT NULL,
    proyecto_id integer NOT NULL
);


ALTER TABLE colaboradores_360_roles OWNER TO suidi;

--
-- TOC entry 230 (class 1259 OID 24388)
-- Name: colaboradores_360_roles_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE colaboradores_360_roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE colaboradores_360_roles_id_seq OWNER TO suidi;

--
-- TOC entry 3422 (class 0 OID 0)
-- Dependencies: 230
-- Name: colaboradores_360_roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE colaboradores_360_roles_id_seq OWNED BY colaboradores_360_roles.id;


--
-- TOC entry 185 (class 1259 OID 16428)
-- Name: colaboradores_colaboradores; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_colaboradores (
    id integer NOT NULL,
    apellido character varying(45) NOT NULL,
    email character varying(254) NOT NULL,
    enviados smallint NOT NULL,
    estado boolean NOT NULL,
    key character varying(64) NOT NULL,
    movil character varying(32),
    nombre character varying(45) NOT NULL,
    propension double precision NOT NULL,
    proyecto_id integer NOT NULL,
    reenviados smallint NOT NULL,
    res_salud smallint NOT NULL,
    respuestas smallint NOT NULL,
    zdel timestamp with time zone,
    puntaje double precision NOT NULL,
    CONSTRAINT colaboradores_colaboradores_enviados_check CHECK ((enviados >= 0)),
    CONSTRAINT colaboradores_colaboradores_reenviados_check CHECK ((reenviados >= 0)),
    CONSTRAINT colaboradores_colaboradores_res_salud_check CHECK ((res_salud >= 0)),
    CONSTRAINT colaboradores_colaboradores_respuestas_check CHECK ((respuestas >= 0))
);


ALTER TABLE colaboradores_colaboradores OWNER TO suidi;

--
-- TOC entry 186 (class 1259 OID 16435)
-- Name: colaboradores_colaboradores_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE colaboradores_colaboradores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE colaboradores_colaboradores_id_seq OWNER TO suidi;

--
-- TOC entry 3425 (class 0 OID 0)
-- Dependencies: 186
-- Name: colaboradores_colaboradores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE colaboradores_colaboradores_id_seq OWNED BY colaboradores_colaboradores.id;


--
-- TOC entry 187 (class 1259 OID 16437)
-- Name: colaboradores_datos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_datos (
    id_id integer NOT NULL,
    area character varying(200),
    cargo character varying(200),
    fec_ingreso date,
    fec_nacimiento date,
    genero character varying(10),
    niv_academico character varying(50),
    opcional1 character varying(100),
    opcional2 character varying(100),
    opcional3 character varying(100),
    opcional4 character varying(100),
    opcional5 character varying(100),
    ciudad character varying(100),
    profesion character varying(200),
    regional character varying(200)
);


ALTER TABLE colaboradores_datos OWNER TO suidi;

--
-- TOC entry 188 (class 1259 OID 16443)
-- Name: colaboradores_metricas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE colaboradores_metricas (
    id_id integer NOT NULL,
    propension text NOT NULL
);


ALTER TABLE colaboradores_metricas OWNER TO suidi;

--
-- TOC entry 235 (class 1259 OID 24408)
-- Name: cuestionarios_360_dimensiones; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_360_dimensiones (
    id integer NOT NULL,
    descripcion text,
    estado boolean NOT NULL,
    instrumento_id integer,
    max_variables smallint NOT NULL,
    nombre character varying(255) NOT NULL,
    posicion smallint,
    proyecto_id integer,
    zdel timestamp with time zone,
    CONSTRAINT cuestionarios_360_dimensiones_max_variables_check CHECK ((max_variables >= 0)),
    CONSTRAINT cuestionarios_360_dimensiones_posicion_check CHECK ((posicion >= 0))
);


ALTER TABLE cuestionarios_360_dimensiones OWNER TO suidi;

--
-- TOC entry 234 (class 1259 OID 24406)
-- Name: cuestionarios_360_dimensiones_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_360_dimensiones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_360_dimensiones_id_seq OWNER TO suidi;

--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 234
-- Name: cuestionarios_360_dimensiones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_360_dimensiones_id_seq OWNED BY cuestionarios_360_dimensiones.id;


--
-- TOC entry 233 (class 1259 OID 24398)
-- Name: cuestionarios_360_instrumentos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_360_instrumentos (
    id integer NOT NULL,
    estado boolean NOT NULL,
    max_dimensiones smallint NOT NULL,
    max_preguntas smallint NOT NULL,
    nombre character varying(255) NOT NULL,
    proyecto_id integer,
    zdel timestamp with time zone,
    CONSTRAINT cuestionarios_360_instrumentos_max_dimensiones_check CHECK ((max_dimensiones >= 0)),
    CONSTRAINT cuestionarios_360_instrumentos_max_preguntas_check CHECK ((max_preguntas >= 0))
);


ALTER TABLE cuestionarios_360_instrumentos OWNER TO suidi;

--
-- TOC entry 232 (class 1259 OID 24396)
-- Name: cuestionarios_360_instrumentos_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_360_instrumentos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_360_instrumentos_id_seq OWNER TO suidi;

--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 232
-- Name: cuestionarios_360_instrumentos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_360_instrumentos_id_seq OWNED BY cuestionarios_360_instrumentos.id;


--
-- TOC entry 239 (class 1259 OID 24434)
-- Name: cuestionarios_360_preguntas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_360_preguntas (
    id integer NOT NULL,
    abierta boolean NOT NULL,
    dimension_id integer,
    estado boolean NOT NULL,
    instrumento_id integer,
    multiple boolean NOT NULL,
    numerica boolean NOT NULL,
    posicion integer NOT NULL,
    puntaje double precision NOT NULL,
    texto character varying(255) NOT NULL,
    variable_id integer,
    proyecto_id integer,
    zdel timestamp with time zone,
    cuerpo boolean DEFAULT false NOT NULL
);


ALTER TABLE cuestionarios_360_preguntas OWNER TO suidi;

--
-- TOC entry 238 (class 1259 OID 24432)
-- Name: cuestionarios_360_preguntas_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_360_preguntas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_360_preguntas_id_seq OWNER TO suidi;

--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 238
-- Name: cuestionarios_360_preguntas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_360_preguntas_id_seq OWNED BY cuestionarios_360_preguntas.id;


--
-- TOC entry 241 (class 1259 OID 24442)
-- Name: cuestionarios_360_respuestas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_360_respuestas (
    id integer NOT NULL,
    numerico double precision,
    pregunta_id integer NOT NULL,
    texto character varying(255) NOT NULL
);


ALTER TABLE cuestionarios_360_respuestas OWNER TO suidi;

--
-- TOC entry 240 (class 1259 OID 24440)
-- Name: cuestionarios_360_respuestas_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_360_respuestas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_360_respuestas_id_seq OWNER TO suidi;

--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 240
-- Name: cuestionarios_360_respuestas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_360_respuestas_id_seq OWNED BY cuestionarios_360_respuestas.id;


--
-- TOC entry 237 (class 1259 OID 24421)
-- Name: cuestionarios_360_variables; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_360_variables (
    id integer NOT NULL,
    descripcion text,
    dimension_id integer,
    estado boolean NOT NULL,
    instrumento_id integer,
    max_preguntas smallint NOT NULL,
    nombre character varying(255) NOT NULL,
    posicion smallint,
    proyecto_id integer,
    zdel timestamp with time zone,
    imagen character varying(400),
    CONSTRAINT cuestionarios_360_variables_max_preguntas_check CHECK ((max_preguntas >= 0)),
    CONSTRAINT cuestionarios_360_variables_posicion_check CHECK ((posicion >= 0))
);


ALTER TABLE cuestionarios_360_variables OWNER TO suidi;

--
-- TOC entry 236 (class 1259 OID 24419)
-- Name: cuestionarios_360_variables_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_360_variables_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_360_variables_id_seq OWNER TO suidi;

--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 236
-- Name: cuestionarios_360_variables_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_360_variables_id_seq OWNED BY cuestionarios_360_variables.id;


--
-- TOC entry 189 (class 1259 OID 16449)
-- Name: cuestionarios_preguntas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_preguntas (
    id integer NOT NULL,
    abierta boolean NOT NULL,
    estado boolean NOT NULL,
    multiple boolean NOT NULL,
    numerica boolean NOT NULL,
    posicion integer NOT NULL,
    texto character varying(255) NOT NULL,
    variable_id integer NOT NULL,
    zdel timestamp with time zone,
    puntaje double precision NOT NULL,
    cuerpo boolean DEFAULT false NOT NULL
);


ALTER TABLE cuestionarios_preguntas OWNER TO suidi;

--
-- TOC entry 190 (class 1259 OID 16452)
-- Name: cuestionarios_preguntas_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_preguntas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_preguntas_id_seq OWNER TO suidi;

--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 190
-- Name: cuestionarios_preguntas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_preguntas_id_seq OWNED BY cuestionarios_preguntas.id;


--
-- TOC entry 191 (class 1259 OID 16454)
-- Name: cuestionarios_proyectos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_proyectos (
    id integer NOT NULL,
    activo boolean NOT NULL,
    can_envio integer NOT NULL,
    empresa_id integer NOT NULL,
    fec_registro timestamp with time zone NOT NULL,
    iniciable boolean NOT NULL,
    interna boolean NOT NULL,
    max_variables smallint NOT NULL,
    nombre character varying(255) NOT NULL,
    prudenciamax double precision NOT NULL,
    prudenciamin double precision NOT NULL,
    tipo character varying(15) NOT NULL,
    tot_preguntas smallint NOT NULL,
    tot_participantes integer NOT NULL,
    tot_aresponder integer NOT NULL,
    tot_respuestas integer NOT NULL,
    total double precision NOT NULL,
    key character varying(64),
    zdel timestamp with time zone,
    pordenadas boolean NOT NULL,
    ciclos smallint DEFAULT 1 NOT NULL,
    ciclico boolean DEFAULT false NOT NULL,
    CONSTRAINT cuestionarios_proyectos_max_variables_check CHECK ((max_variables >= 0)),
    CONSTRAINT cuestionarios_proyectos_tot_participantes_check CHECK ((tot_participantes >= 0)),
    CONSTRAINT cuestionarios_proyectos_tot_preguntas_check CHECK ((tot_preguntas >= 0))
);


ALTER TABLE cuestionarios_proyectos OWNER TO suidi;

--
-- TOC entry 192 (class 1259 OID 16460)
-- Name: cuestionarios_proyectos_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_proyectos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_proyectos_id_seq OWNER TO suidi;

--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 192
-- Name: cuestionarios_proyectos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_proyectos_id_seq OWNED BY cuestionarios_proyectos.id;


--
-- TOC entry 193 (class 1259 OID 16462)
-- Name: cuestionarios_proyectos_usuarios; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_proyectos_usuarios (
    id integer NOT NULL,
    proyectos_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE cuestionarios_proyectos_usuarios OWNER TO suidi;

--
-- TOC entry 194 (class 1259 OID 16465)
-- Name: cuestionarios_proyectos_usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_proyectos_usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_proyectos_usuarios_id_seq OWNER TO suidi;

--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 194
-- Name: cuestionarios_proyectos_usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_proyectos_usuarios_id_seq OWNED BY cuestionarios_proyectos_usuarios.id;


--
-- TOC entry 195 (class 1259 OID 16467)
-- Name: cuestionarios_respuestas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_respuestas (
    id integer NOT NULL,
    numerico double precision,
    pregunta_id integer NOT NULL,
    texto character varying(255) NOT NULL
);


ALTER TABLE cuestionarios_respuestas OWNER TO suidi;

--
-- TOC entry 196 (class 1259 OID 16470)
-- Name: cuestionarios_respuestas_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_respuestas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_respuestas_id_seq OWNER TO suidi;

--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 196
-- Name: cuestionarios_respuestas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_respuestas_id_seq OWNED BY cuestionarios_respuestas.id;


--
-- TOC entry 197 (class 1259 OID 16472)
-- Name: cuestionarios_variables; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE cuestionarios_variables (
    id integer NOT NULL,
    descripcion text,
    estado boolean NOT NULL,
    max_preguntas smallint NOT NULL,
    nombre character varying(255) NOT NULL,
    posicion smallint,
    proyecto_id integer,
    zdel timestamp with time zone,
    CONSTRAINT cuestionarios_variables_max_preguntas_check CHECK ((max_preguntas >= 0)),
    CONSTRAINT cuestionarios_variables_posicion_check CHECK ((posicion >= 0))
);


ALTER TABLE cuestionarios_variables OWNER TO suidi;

--
-- TOC entry 198 (class 1259 OID 16480)
-- Name: cuestionarios_variables_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE cuestionarios_variables_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cuestionarios_variables_id_seq OWNER TO suidi;

--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 198
-- Name: cuestionarios_variables_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE cuestionarios_variables_id_seq OWNED BY cuestionarios_variables.id;


--
-- TOC entry 199 (class 1259 OID 16482)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO suidi;

--
-- TOC entry 200 (class 1259 OID 16489)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO suidi;

--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 200
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- TOC entry 201 (class 1259 OID 16491)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO suidi;

--
-- TOC entry 202 (class 1259 OID 16494)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO suidi;

--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 203 (class 1259 OID 16496)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO suidi;

--
-- TOC entry 204 (class 1259 OID 16502)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO suidi;

--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 204
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- TOC entry 205 (class 1259 OID 16504)
-- Name: django_session; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO suidi;

--
-- TOC entry 243 (class 1259 OID 24450)
-- Name: mensajeria_360_streaming; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE mensajeria_360_streaming (
    id integer NOT NULL,
    colaborador_id integer NOT NULL,
    evaluado_id integer,
    contestadas smallint NOT NULL,
    instrumento_id integer NOT NULL,
    pregunta_id integer NOT NULL,
    proyecto_id integer NOT NULL,
    red_id integer NOT NULL,
    fec_controlenvio timestamp with time zone,
    fecharespuesta timestamp with time zone,
    respuesta text,
    CONSTRAINT mensajeria_360_streaming_contestadas_check CHECK ((contestadas >= 0))
);


ALTER TABLE mensajeria_360_streaming OWNER TO suidi;

--
-- TOC entry 242 (class 1259 OID 24448)
-- Name: mensajeria_360_streaming_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE mensajeria_360_streaming_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mensajeria_360_streaming_id_seq OWNER TO suidi;

--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 242
-- Name: mensajeria_360_streaming_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE mensajeria_360_streaming_id_seq OWNED BY mensajeria_360_streaming.id;


--
-- TOC entry 206 (class 1259 OID 16510)
-- Name: mensajeria_externa; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE mensajeria_externa (
    id integer NOT NULL,
    colaborador integer NOT NULL,
    proyecto_id integer NOT NULL,
    pregunta_id integer NOT NULL,
    fecharespuesta timestamp with time zone,
    respuesta text
);


ALTER TABLE mensajeria_externa OWNER TO suidi;

--
-- TOC entry 207 (class 1259 OID 16516)
-- Name: mensajeria_externa_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE mensajeria_externa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mensajeria_externa_id_seq OWNER TO suidi;

--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 207
-- Name: mensajeria_externa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE mensajeria_externa_id_seq OWNED BY mensajeria_externa.id;


--
-- TOC entry 208 (class 1259 OID 16518)
-- Name: mensajeria_metricasexterna; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE mensajeria_metricasexterna (
    id integer NOT NULL,
    acumulado integer NOT NULL,
    encuestados integer NOT NULL,
    fecha date NOT NULL,
    proyecto_id integer NOT NULL
);


ALTER TABLE mensajeria_metricasexterna OWNER TO suidi;

--
-- TOC entry 209 (class 1259 OID 16521)
-- Name: mensajeria_metricasexterna_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE mensajeria_metricasexterna_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mensajeria_metricasexterna_id_seq OWNER TO suidi;

--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 209
-- Name: mensajeria_metricasexterna_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE mensajeria_metricasexterna_id_seq OWNED BY mensajeria_metricasexterna.id;


--
-- TOC entry 210 (class 1259 OID 16523)
-- Name: mensajeria_srs; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE mensajeria_srs (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    fecharespuesta timestamp with time zone NOT NULL,
    respuesta text
);


ALTER TABLE mensajeria_srs OWNER TO suidi;

--
-- TOC entry 211 (class 1259 OID 16529)
-- Name: mensajeria_srs_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE mensajeria_srs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mensajeria_srs_id_seq OWNER TO suidi;

--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 211
-- Name: mensajeria_srs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE mensajeria_srs_id_seq OWNED BY mensajeria_srs.id;


--
-- TOC entry 212 (class 1259 OID 16531)
-- Name: mensajeria_streaming; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE mensajeria_streaming (
    id integer NOT NULL,
    colaborador_id integer NOT NULL,
    pregunta_id integer NOT NULL,
    proyecto_id integer NOT NULL,
    fec_controlenvio timestamp with time zone,
    fecharespuesta timestamp with time zone,
    respuesta text
);


ALTER TABLE mensajeria_streaming OWNER TO suidi;

--
-- TOC entry 213 (class 1259 OID 16537)
-- Name: mensajeria_streaming_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE mensajeria_streaming_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE mensajeria_streaming_id_seq OWNER TO suidi;

--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 213
-- Name: mensajeria_streaming_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE mensajeria_streaming_id_seq OWNED BY mensajeria_streaming.id;


--
-- TOC entry 245 (class 1259 OID 24462)
-- Name: redes_360_redes; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE redes_360_redes (
    id integer NOT NULL,
    colaborador_id integer NOT NULL,
    estado boolean NOT NULL,
    evaluado_id integer NOT NULL,
    instrumento_id integer,
    proyecto_id integer NOT NULL,
    rol character varying(128),
    rol_idn integer,
    pre_respuestas smallint NOT NULL,
    tot_porcentaje double precision NOT NULL,
    CONSTRAINT redes_360_redes_pre_respuestas_check CHECK ((pre_respuestas >= 0)),
    CONSTRAINT redes_360_redes_rol_idn_check CHECK ((rol_idn >= 0))
);


ALTER TABLE redes_360_redes OWNER TO suidi;

--
-- TOC entry 244 (class 1259 OID 24460)
-- Name: redes_360_redes_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE redes_360_redes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE redes_360_redes_id_seq OWNER TO suidi;

--
-- TOC entry 3485 (class 0 OID 0)
-- Dependencies: 244
-- Name: redes_360_redes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE redes_360_redes_id_seq OWNED BY redes_360_redes.id;


--
-- TOC entry 214 (class 1259 OID 16539)
-- Name: usuarios_empresas; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_empresas (
    id integer NOT NULL,
    departamento character varying(100),
    nit character varying(20),
    nombre character varying(100) NOT NULL,
    num_empleados integer,
    pagina character varying(1000),
    pais character varying(100),
    sector character varying(100),
    usuario_id integer NOT NULL,
    zdel timestamp with time zone
);


ALTER TABLE usuarios_empresas OWNER TO suidi;

--
-- TOC entry 215 (class 1259 OID 16545)
-- Name: usuarios_empresas_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE usuarios_empresas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuarios_empresas_id_seq OWNER TO suidi;

--
-- TOC entry 3488 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuarios_empresas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE usuarios_empresas_id_seq OWNED BY usuarios_empresas.id;


--
-- TOC entry 216 (class 1259 OID 16547)
-- Name: usuarios_errores; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_errores (
    id integer NOT NULL,
    usuario character varying(500) NOT NULL,
    reporte text NOT NULL,
    imagen character varying(100),
    fregistro timestamp with time zone NOT NULL
);


ALTER TABLE usuarios_errores OWNER TO suidi;

--
-- TOC entry 217 (class 1259 OID 16553)
-- Name: usuarios_errores_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE usuarios_errores_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuarios_errores_id_seq OWNER TO suidi;

--
-- TOC entry 3491 (class 0 OID 0)
-- Dependencies: 217
-- Name: usuarios_errores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE usuarios_errores_id_seq OWNED BY usuarios_errores.id;


--
-- TOC entry 218 (class 1259 OID 16555)
-- Name: usuarios_indice; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_indice (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    name character varying(100) NOT NULL,
    parent_id integer,
    lft integer NOT NULL,
    rght integer NOT NULL,
    tree_id integer NOT NULL,
    level integer NOT NULL,
    CONSTRAINT usuarios_indice_level_check CHECK ((level >= 0)),
    CONSTRAINT usuarios_indice_lft_check CHECK ((lft >= 0)),
    CONSTRAINT usuarios_indice_rght_check CHECK ((rght >= 0)),
    CONSTRAINT usuarios_indice_tree_id_check CHECK ((tree_id >= 0))
);


ALTER TABLE usuarios_indice OWNER TO suidi;

--
-- TOC entry 219 (class 1259 OID 16562)
-- Name: usuarios_indice_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE usuarios_indice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuarios_indice_id_seq OWNER TO suidi;

--
-- TOC entry 3494 (class 0 OID 0)
-- Dependencies: 219
-- Name: usuarios_indice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE usuarios_indice_id_seq OWNED BY usuarios_indice.id;


--
-- TOC entry 220 (class 1259 OID 16564)
-- Name: usuarios_logs; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_logs (
    id integer NOT NULL,
    usuario character varying(1000) NOT NULL,
    usuario_username character varying(1000) NOT NULL,
    accion text NOT NULL,
    descripcion text NOT NULL,
    fregistro timestamp with time zone NOT NULL
);


ALTER TABLE usuarios_logs OWNER TO suidi;

--
-- TOC entry 221 (class 1259 OID 16570)
-- Name: usuarios_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE usuarios_logs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuarios_logs_id_seq OWNER TO suidi;

--
-- TOC entry 3497 (class 0 OID 0)
-- Dependencies: 221
-- Name: usuarios_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE usuarios_logs_id_seq OWNED BY usuarios_logs.id;


--
-- TOC entry 222 (class 1259 OID 16572)
-- Name: usuarios_permisos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_permisos (
    id_id integer NOT NULL,
    consultor boolean NOT NULL,
    cre_usuarios boolean NOT NULL,
    act_surveys boolean NOT NULL,
    act_variables boolean NOT NULL,
    col_add boolean NOT NULL,
    col_del boolean NOT NULL,
    col_edit boolean NOT NULL,
    col_see boolean NOT NULL,
    det_see boolean NOT NULL,
    max_proyectos smallint NOT NULL,
    max_pro_usados smallint NOT NULL,
    red_add boolean NOT NULL,
    red_del boolean NOT NULL,
    red_edit boolean NOT NULL,
    red_see boolean NOT NULL,
    pro_add boolean NOT NULL,
    pro_del boolean NOT NULL,
    pro_edit boolean NOT NULL,
    pro_see boolean NOT NULL,
    res_exp boolean NOT NULL,
    res_see boolean NOT NULL,
    var_add boolean NOT NULL,
    var_del boolean NOT NULL,
    var_edit boolean NOT NULL,
    var_see boolean NOT NULL,
    CONSTRAINT usuarios_permisos_max_pro_usados_check CHECK ((max_pro_usados >= 0)),
    CONSTRAINT usuarios_permisos_max_proyectos_check CHECK ((max_proyectos >= 0))
);


ALTER TABLE usuarios_permisos OWNER TO suidi;

--
-- TOC entry 223 (class 1259 OID 16577)
-- Name: usuarios_proyectosdatos; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_proyectosdatos (
    asunto character varying(75),
    id_id integer NOT NULL,
    cue_correo text,
    fregistro date NOT NULL,
    int_encuesta text,
    logo character varying(100) NOT NULL,
    logoenc character varying(100),
    censo boolean NOT NULL,
    tit_encuesta character varying(255),
    opcional1 character varying(100),
    opcional2 character varying(100),
    opcional3 character varying(100),
    opcional4 character varying(100),
    opcional5 character varying(100),
    finicio date,
    ffin date,
    msm boolean NOT NULL
);


ALTER TABLE usuarios_proyectosdatos OWNER TO suidi;

--
-- TOC entry 224 (class 1259 OID 16583)
-- Name: usuarios_recuperar; Type: TABLE; Schema: public; Owner: suidi
--

CREATE TABLE usuarios_recuperar (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    link character varying(96) NOT NULL,
    fregistro timestamp with time zone NOT NULL
);


ALTER TABLE usuarios_recuperar OWNER TO suidi;

--
-- TOC entry 225 (class 1259 OID 16586)
-- Name: usuarios_recuperar_id_seq; Type: SEQUENCE; Schema: public; Owner: suidi
--

CREATE SEQUENCE usuarios_recuperar_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE usuarios_recuperar_id_seq OWNER TO suidi;

--
-- TOC entry 3502 (class 0 OID 0)
-- Dependencies: 225
-- Name: usuarios_recuperar_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: suidi
--

ALTER SEQUENCE usuarios_recuperar_id_seq OWNED BY usuarios_recuperar.id;


--
-- TOC entry 2995 (class 2604 OID 16588)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- TOC entry 2996 (class 2604 OID 16589)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 2997 (class 2604 OID 16590)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- TOC entry 2998 (class 2604 OID 16591)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- TOC entry 2999 (class 2604 OID 16592)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- TOC entry 3000 (class 2604 OID 16593)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 3038 (class 2604 OID 24358)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_colaboradores ALTER COLUMN id SET DEFAULT nextval('colaboradores_360_colaboradores_id_seq'::regclass);


--
-- TOC entry 3047 (class 2604 OID 24393)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_roles ALTER COLUMN id SET DEFAULT nextval('colaboradores_360_roles_id_seq'::regclass);


--
-- TOC entry 3001 (class 2604 OID 16594)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_colaboradores ALTER COLUMN id SET DEFAULT nextval('colaboradores_colaboradores_id_seq'::regclass);


--
-- TOC entry 3051 (class 2604 OID 24411)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_dimensiones ALTER COLUMN id SET DEFAULT nextval('cuestionarios_360_dimensiones_id_seq'::regclass);


--
-- TOC entry 3048 (class 2604 OID 24401)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_instrumentos ALTER COLUMN id SET DEFAULT nextval('cuestionarios_360_instrumentos_id_seq'::regclass);


--
-- TOC entry 3057 (class 2604 OID 24437)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas ALTER COLUMN id SET DEFAULT nextval('cuestionarios_360_preguntas_id_seq'::regclass);


--
-- TOC entry 3059 (class 2604 OID 24445)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_respuestas ALTER COLUMN id SET DEFAULT nextval('cuestionarios_360_respuestas_id_seq'::regclass);


--
-- TOC entry 3054 (class 2604 OID 24424)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_variables ALTER COLUMN id SET DEFAULT nextval('cuestionarios_360_variables_id_seq'::regclass);


--
-- TOC entry 3006 (class 2604 OID 16596)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_preguntas ALTER COLUMN id SET DEFAULT nextval('cuestionarios_preguntas_id_seq'::regclass);


--
-- TOC entry 3008 (class 2604 OID 16597)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos ALTER COLUMN id SET DEFAULT nextval('cuestionarios_proyectos_id_seq'::regclass);


--
-- TOC entry 3014 (class 2604 OID 16598)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos_usuarios ALTER COLUMN id SET DEFAULT nextval('cuestionarios_proyectos_usuarios_id_seq'::regclass);


--
-- TOC entry 3015 (class 2604 OID 16599)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_respuestas ALTER COLUMN id SET DEFAULT nextval('cuestionarios_respuestas_id_seq'::regclass);


--
-- TOC entry 3016 (class 2604 OID 16600)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_variables ALTER COLUMN id SET DEFAULT nextval('cuestionarios_variables_id_seq'::regclass);


--
-- TOC entry 3019 (class 2604 OID 16601)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- TOC entry 3021 (class 2604 OID 16602)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 3022 (class 2604 OID 16603)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- TOC entry 3060 (class 2604 OID 24453)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming ALTER COLUMN id SET DEFAULT nextval('mensajeria_360_streaming_id_seq'::regclass);


--
-- TOC entry 3023 (class 2604 OID 16604)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_externa ALTER COLUMN id SET DEFAULT nextval('mensajeria_externa_id_seq'::regclass);


--
-- TOC entry 3024 (class 2604 OID 16605)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_metricasexterna ALTER COLUMN id SET DEFAULT nextval('mensajeria_metricasexterna_id_seq'::regclass);


--
-- TOC entry 3025 (class 2604 OID 16606)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_srs ALTER COLUMN id SET DEFAULT nextval('mensajeria_srs_id_seq'::regclass);


--
-- TOC entry 3026 (class 2604 OID 16607)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_streaming ALTER COLUMN id SET DEFAULT nextval('mensajeria_streaming_id_seq'::regclass);


--
-- TOC entry 3062 (class 2604 OID 24465)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes ALTER COLUMN id SET DEFAULT nextval('redes_360_redes_id_seq'::regclass);


--
-- TOC entry 3027 (class 2604 OID 16608)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_empresas ALTER COLUMN id SET DEFAULT nextval('usuarios_empresas_id_seq'::regclass);


--
-- TOC entry 3028 (class 2604 OID 16609)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_errores ALTER COLUMN id SET DEFAULT nextval('usuarios_errores_id_seq'::regclass);


--
-- TOC entry 3029 (class 2604 OID 16610)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_indice ALTER COLUMN id SET DEFAULT nextval('usuarios_indice_id_seq'::regclass);


--
-- TOC entry 3034 (class 2604 OID 16611)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_logs ALTER COLUMN id SET DEFAULT nextval('usuarios_logs_id_seq'::regclass);


--
-- TOC entry 3037 (class 2604 OID 16612)
-- Name: id; Type: DEFAULT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_recuperar ALTER COLUMN id SET DEFAULT nextval('usuarios_recuperar_id_seq'::regclass);


--
-- TOC entry 3067 (class 2606 OID 16614)
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3073 (class 2606 OID 16616)
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- TOC entry 3075 (class 2606 OID 16618)
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3069 (class 2606 OID 16620)
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3078 (class 2606 OID 16622)
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- TOC entry 3080 (class 2606 OID 16624)
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3089 (class 2606 OID 16626)
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3091 (class 2606 OID 16628)
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- TOC entry 3082 (class 2606 OID 16630)
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3095 (class 2606 OID 16632)
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3097 (class 2606 OID 16634)
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- TOC entry 3085 (class 2606 OID 16636)
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3179 (class 2606 OID 24370)
-- Name: colaboradores_360_colaboradores_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_colaboradores
    ADD CONSTRAINT colaboradores_360_colaboradores_pkey PRIMARY KEY (id);


--
-- TOC entry 3181 (class 2606 OID 24378)
-- Name: colaboradores_360_datos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_datos
    ADD CONSTRAINT colaboradores_360_datos_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3183 (class 2606 OID 24387)
-- Name: colaboradores_360_metricas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_metricas
    ADD CONSTRAINT colaboradores_360_metricas_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3186 (class 2606 OID 24395)
-- Name: colaboradores_360_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_roles
    ADD CONSTRAINT colaboradores_360_roles_pkey PRIMARY KEY (id);


--
-- TOC entry 3100 (class 2606 OID 16638)
-- Name: colaboradores_colaboradores_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_colaboradores
    ADD CONSTRAINT colaboradores_colaboradores_pkey PRIMARY KEY (id);


--
-- TOC entry 3102 (class 2606 OID 16640)
-- Name: colaboradores_datos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_datos
    ADD CONSTRAINT colaboradores_datos_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3104 (class 2606 OID 16642)
-- Name: colaboradores_metricas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_metricas
    ADD CONSTRAINT colaboradores_metricas_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3195 (class 2606 OID 24418)
-- Name: cuestionarios_360_dimensiones_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_dimensiones
    ADD CONSTRAINT cuestionarios_360_dimensiones_pkey PRIMARY KEY (id);


--
-- TOC entry 3191 (class 2606 OID 24405)
-- Name: cuestionarios_360_instrumentos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_instrumentos
    ADD CONSTRAINT cuestionarios_360_instrumentos_pkey PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 24439)
-- Name: cuestionarios_360_preguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas
    ADD CONSTRAINT cuestionarios_360_preguntas_pkey PRIMARY KEY (id);


--
-- TOC entry 3209 (class 2606 OID 24447)
-- Name: cuestionarios_360_respuestas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_respuestas
    ADD CONSTRAINT cuestionarios_360_respuestas_pkey PRIMARY KEY (id);


--
-- TOC entry 3200 (class 2606 OID 24431)
-- Name: cuestionarios_360_variables_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_variables
    ADD CONSTRAINT cuestionarios_360_variables_pkey PRIMARY KEY (id);


--
-- TOC entry 3107 (class 2606 OID 16644)
-- Name: cuestionarios_preguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_preguntas
    ADD CONSTRAINT cuestionarios_preguntas_pkey PRIMARY KEY (id);


--
-- TOC entry 3110 (class 2606 OID 16646)
-- Name: cuestionarios_proyectos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos
    ADD CONSTRAINT cuestionarios_proyectos_pkey PRIMARY KEY (id);


--
-- TOC entry 3114 (class 2606 OID 16648)
-- Name: cuestionarios_proyectos_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos_usuarios
    ADD CONSTRAINT cuestionarios_proyectos_usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 3116 (class 2606 OID 16650)
-- Name: cuestionarios_proyectos_usuarios_proyectos_id_user_id_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos_usuarios
    ADD CONSTRAINT cuestionarios_proyectos_usuarios_proyectos_id_user_id_key UNIQUE (proyectos_id, user_id);


--
-- TOC entry 3119 (class 2606 OID 16652)
-- Name: cuestionarios_respuestas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_respuestas
    ADD CONSTRAINT cuestionarios_respuestas_pkey PRIMARY KEY (id);


--
-- TOC entry 3122 (class 2606 OID 16654)
-- Name: cuestionarios_variables_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_variables
    ADD CONSTRAINT cuestionarios_variables_pkey PRIMARY KEY (id);


--
-- TOC entry 3126 (class 2606 OID 16656)
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3128 (class 2606 OID 16658)
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- TOC entry 3130 (class 2606 OID 16660)
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3132 (class 2606 OID 16662)
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3135 (class 2606 OID 16664)
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3217 (class 2606 OID 24459)
-- Name: mensajeria_360_streaming_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT mensajeria_360_streaming_pkey PRIMARY KEY (id);


--
-- TOC entry 3140 (class 2606 OID 16666)
-- Name: mensajeria_externa_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_externa
    ADD CONSTRAINT mensajeria_externa_pkey PRIMARY KEY (id);


--
-- TOC entry 3143 (class 2606 OID 16668)
-- Name: mensajeria_metricasexterna_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_metricasexterna
    ADD CONSTRAINT mensajeria_metricasexterna_pkey PRIMARY KEY (id);


--
-- TOC entry 3146 (class 2606 OID 16670)
-- Name: mensajeria_srs_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_srs
    ADD CONSTRAINT mensajeria_srs_pkey PRIMARY KEY (id);


--
-- TOC entry 3151 (class 2606 OID 16672)
-- Name: mensajeria_streaming_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_streaming
    ADD CONSTRAINT mensajeria_streaming_pkey PRIMARY KEY (id);


--
-- TOC entry 3224 (class 2606 OID 24469)
-- Name: redes_360_redes_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes
    ADD CONSTRAINT redes_360_redes_pkey PRIMARY KEY (id);


--
-- TOC entry 3154 (class 2606 OID 16674)
-- Name: usuarios_empresas_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_empresas
    ADD CONSTRAINT usuarios_empresas_pkey PRIMARY KEY (id);


--
-- TOC entry 3156 (class 2606 OID 16676)
-- Name: usuarios_errores_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_errores
    ADD CONSTRAINT usuarios_errores_pkey PRIMARY KEY (id);


--
-- TOC entry 3165 (class 2606 OID 16678)
-- Name: usuarios_indice_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_indice
    ADD CONSTRAINT usuarios_indice_pkey PRIMARY KEY (id);


--
-- TOC entry 3167 (class 2606 OID 16680)
-- Name: usuarios_indice_usuario_id_key; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_indice
    ADD CONSTRAINT usuarios_indice_usuario_id_key UNIQUE (usuario_id);


--
-- TOC entry 3169 (class 2606 OID 16682)
-- Name: usuarios_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_logs
    ADD CONSTRAINT usuarios_logs_pkey PRIMARY KEY (id);


--
-- TOC entry 3171 (class 2606 OID 16684)
-- Name: usuarios_permisos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_permisos
    ADD CONSTRAINT usuarios_permisos_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3173 (class 2606 OID 16686)
-- Name: usuarios_proyectosdatos_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_proyectosdatos
    ADD CONSTRAINT usuarios_proyectosdatos_pkey PRIMARY KEY (id_id);


--
-- TOC entry 3176 (class 2606 OID 16688)
-- Name: usuarios_recuperar_pkey; Type: CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_recuperar
    ADD CONSTRAINT usuarios_recuperar_pkey PRIMARY KEY (id);


--
-- TOC entry 3065 (class 1259 OID 16689)
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3070 (class 1259 OID 16690)
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- TOC entry 3071 (class 1259 OID 16691)
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3076 (class 1259 OID 16692)
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- TOC entry 3086 (class 1259 OID 16693)
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- TOC entry 3087 (class 1259 OID 16694)
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- TOC entry 3092 (class 1259 OID 16695)
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3093 (class 1259 OID 16696)
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3083 (class 1259 OID 16697)
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3177 (class 1259 OID 24475)
-- Name: colaboradores_360_colaboradores_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX colaboradores_360_colaboradores_f543c3f9 ON colaboradores_360_colaboradores USING btree (proyecto_id);


--
-- TOC entry 3184 (class 1259 OID 24491)
-- Name: colaboradores_360_roles_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX colaboradores_360_roles_f543c3f9 ON colaboradores_360_roles USING btree (proyecto_id);


--
-- TOC entry 3098 (class 1259 OID 16698)
-- Name: colaboradores_colaboradores_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX colaboradores_colaboradores_f543c3f9 ON colaboradores_colaboradores USING btree (proyecto_id);


--
-- TOC entry 3192 (class 1259 OID 24510)
-- Name: cuestionarios_360_dimensiones_f2224a23; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_dimensiones_f2224a23 ON cuestionarios_360_dimensiones USING btree (instrumento_id);


--
-- TOC entry 3193 (class 1259 OID 24511)
-- Name: cuestionarios_360_dimensiones_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_dimensiones_f543c3f9 ON cuestionarios_360_dimensiones USING btree (proyecto_id);


--
-- TOC entry 3187 (class 1259 OID 24497)
-- Name: cuestionarios_360_instrumentos_7a675883; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_instrumentos_7a675883 ON cuestionarios_360_instrumentos USING btree (nombre);


--
-- TOC entry 3188 (class 1259 OID 24498)
-- Name: cuestionarios_360_instrumentos_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_instrumentos_f543c3f9 ON cuestionarios_360_instrumentos USING btree (proyecto_id);


--
-- TOC entry 3189 (class 1259 OID 24499)
-- Name: cuestionarios_360_instrumentos_nombre_79e1f4aa5909279a_like; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_instrumentos_nombre_79e1f4aa5909279a_like ON cuestionarios_360_instrumentos USING btree (nombre varchar_pattern_ops);


--
-- TOC entry 3201 (class 1259 OID 24552)
-- Name: cuestionarios_360_preguntas_59bc5ce5; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_preguntas_59bc5ce5 ON cuestionarios_360_preguntas USING btree (variable_id);


--
-- TOC entry 3202 (class 1259 OID 24550)
-- Name: cuestionarios_360_preguntas_b46ef2c7; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_preguntas_b46ef2c7 ON cuestionarios_360_preguntas USING btree (dimension_id);


--
-- TOC entry 3203 (class 1259 OID 24551)
-- Name: cuestionarios_360_preguntas_f2224a23; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_preguntas_f2224a23 ON cuestionarios_360_preguntas USING btree (instrumento_id);


--
-- TOC entry 3204 (class 1259 OID 24553)
-- Name: cuestionarios_360_preguntas_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_preguntas_f543c3f9 ON cuestionarios_360_preguntas USING btree (proyecto_id);


--
-- TOC entry 3207 (class 1259 OID 24559)
-- Name: cuestionarios_360_respuestas_5e7715cc; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_respuestas_5e7715cc ON cuestionarios_360_respuestas USING btree (pregunta_id);


--
-- TOC entry 3196 (class 1259 OID 24527)
-- Name: cuestionarios_360_variables_b46ef2c7; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_variables_b46ef2c7 ON cuestionarios_360_variables USING btree (dimension_id);


--
-- TOC entry 3197 (class 1259 OID 24528)
-- Name: cuestionarios_360_variables_f2224a23; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_variables_f2224a23 ON cuestionarios_360_variables USING btree (instrumento_id);


--
-- TOC entry 3198 (class 1259 OID 24529)
-- Name: cuestionarios_360_variables_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_360_variables_f543c3f9 ON cuestionarios_360_variables USING btree (proyecto_id);


--
-- TOC entry 3105 (class 1259 OID 16699)
-- Name: cuestionarios_preguntas_59bc5ce5; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_preguntas_59bc5ce5 ON cuestionarios_preguntas USING btree (variable_id);


--
-- TOC entry 3108 (class 1259 OID 16700)
-- Name: cuestionarios_proyectos_e8f8b1ef; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_proyectos_e8f8b1ef ON cuestionarios_proyectos USING btree (empresa_id);


--
-- TOC entry 3111 (class 1259 OID 16701)
-- Name: cuestionarios_proyectos_usuarios_919a58ba; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_proyectos_usuarios_919a58ba ON cuestionarios_proyectos_usuarios USING btree (proyectos_id);


--
-- TOC entry 3112 (class 1259 OID 16702)
-- Name: cuestionarios_proyectos_usuarios_e8701ad4; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_proyectos_usuarios_e8701ad4 ON cuestionarios_proyectos_usuarios USING btree (user_id);


--
-- TOC entry 3117 (class 1259 OID 16703)
-- Name: cuestionarios_respuestas_5e7715cc; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_respuestas_5e7715cc ON cuestionarios_respuestas USING btree (pregunta_id);


--
-- TOC entry 3120 (class 1259 OID 16704)
-- Name: cuestionarios_variables_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX cuestionarios_variables_f543c3f9 ON cuestionarios_variables USING btree (proyecto_id);


--
-- TOC entry 3123 (class 1259 OID 16705)
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- TOC entry 3124 (class 1259 OID 16706)
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- TOC entry 3133 (class 1259 OID 16707)
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- TOC entry 3136 (class 1259 OID 16708)
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3210 (class 1259 OID 24595)
-- Name: mensajeria_360_streaming_223bf4cf; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_223bf4cf ON mensajeria_360_streaming USING btree (red_id);


--
-- TOC entry 3211 (class 1259 OID 24590)
-- Name: mensajeria_360_streaming_4c506918; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_4c506918 ON mensajeria_360_streaming USING btree (colaborador_id);


--
-- TOC entry 3212 (class 1259 OID 24593)
-- Name: mensajeria_360_streaming_5e7715cc; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_5e7715cc ON mensajeria_360_streaming USING btree (pregunta_id);


--
-- TOC entry 3213 (class 1259 OID 24591)
-- Name: mensajeria_360_streaming_ae853279; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_ae853279 ON mensajeria_360_streaming USING btree (evaluado_id);


--
-- TOC entry 3214 (class 1259 OID 24592)
-- Name: mensajeria_360_streaming_f2224a23; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_f2224a23 ON mensajeria_360_streaming USING btree (instrumento_id);


--
-- TOC entry 3215 (class 1259 OID 24594)
-- Name: mensajeria_360_streaming_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_360_streaming_f543c3f9 ON mensajeria_360_streaming USING btree (proyecto_id);


--
-- TOC entry 3137 (class 1259 OID 16709)
-- Name: mensajeria_externa_5e7715cc; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_externa_5e7715cc ON mensajeria_externa USING btree (pregunta_id);


--
-- TOC entry 3138 (class 1259 OID 16710)
-- Name: mensajeria_externa_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_externa_f543c3f9 ON mensajeria_externa USING btree (proyecto_id);


--
-- TOC entry 3141 (class 1259 OID 16711)
-- Name: mensajeria_metricasexterna_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_metricasexterna_f543c3f9 ON mensajeria_metricasexterna USING btree (proyecto_id);


--
-- TOC entry 3144 (class 1259 OID 16712)
-- Name: mensajeria_srs_abfe0f96; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_srs_abfe0f96 ON mensajeria_srs USING btree (usuario_id);


--
-- TOC entry 3147 (class 1259 OID 16713)
-- Name: mensajeria_streaming_4c506918; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_streaming_4c506918 ON mensajeria_streaming USING btree (colaborador_id);


--
-- TOC entry 3148 (class 1259 OID 16714)
-- Name: mensajeria_streaming_5e7715cc; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_streaming_5e7715cc ON mensajeria_streaming USING btree (pregunta_id);


--
-- TOC entry 3149 (class 1259 OID 16715)
-- Name: mensajeria_streaming_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX mensajeria_streaming_f543c3f9 ON mensajeria_streaming USING btree (proyecto_id);


--
-- TOC entry 3218 (class 1259 OID 24620)
-- Name: redes_360_redes_3c7cfc76; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX redes_360_redes_3c7cfc76 ON redes_360_redes USING btree (rol_idn);


--
-- TOC entry 3219 (class 1259 OID 24616)
-- Name: redes_360_redes_4c506918; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX redes_360_redes_4c506918 ON redes_360_redes USING btree (colaborador_id);


--
-- TOC entry 3220 (class 1259 OID 24617)
-- Name: redes_360_redes_ae853279; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX redes_360_redes_ae853279 ON redes_360_redes USING btree (evaluado_id);


--
-- TOC entry 3221 (class 1259 OID 24618)
-- Name: redes_360_redes_f2224a23; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX redes_360_redes_f2224a23 ON redes_360_redes USING btree (instrumento_id);


--
-- TOC entry 3222 (class 1259 OID 24619)
-- Name: redes_360_redes_f543c3f9; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX redes_360_redes_f543c3f9 ON redes_360_redes USING btree (proyecto_id);


--
-- TOC entry 3152 (class 1259 OID 16716)
-- Name: usuarios_empresas_abfe0f96; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_empresas_abfe0f96 ON usuarios_empresas USING btree (usuario_id);


--
-- TOC entry 3157 (class 1259 OID 16717)
-- Name: usuarios_indice_3cfbd988; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_3cfbd988 ON usuarios_indice USING btree (rght);


--
-- TOC entry 3158 (class 1259 OID 16718)
-- Name: usuarios_indice_656442a0; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_656442a0 ON usuarios_indice USING btree (tree_id);


--
-- TOC entry 3159 (class 1259 OID 16719)
-- Name: usuarios_indice_6be37982; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_6be37982 ON usuarios_indice USING btree (parent_id);


--
-- TOC entry 3160 (class 1259 OID 16720)
-- Name: usuarios_indice_b068931c; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_b068931c ON usuarios_indice USING btree (name);


--
-- TOC entry 3161 (class 1259 OID 16721)
-- Name: usuarios_indice_c9e9a848; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_c9e9a848 ON usuarios_indice USING btree (level);


--
-- TOC entry 3162 (class 1259 OID 16722)
-- Name: usuarios_indice_caf7cc51; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_caf7cc51 ON usuarios_indice USING btree (lft);


--
-- TOC entry 3163 (class 1259 OID 16723)
-- Name: usuarios_indice_name_6a90433aa26dec65_like; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_indice_name_6a90433aa26dec65_like ON usuarios_indice USING btree (name varchar_pattern_ops);


--
-- TOC entry 3174 (class 1259 OID 16724)
-- Name: usuarios_recuperar_abfe0f96; Type: INDEX; Schema: public; Owner: suidi
--

CREATE INDEX usuarios_recuperar_abfe0f96 ON usuarios_recuperar USING btree (usuario_id);


--
-- TOC entry 3277 (class 2606 OID 24596)
-- Name: D312ef7d385dda8a5278d3e8a77fdc36; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes
    ADD CONSTRAINT "D312ef7d385dda8a5278d3e8a77fdc36" FOREIGN KEY (colaborador_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3261 (class 2606 OID 24500)
-- Name: D52be5ea6e9dda03c2e5c101fafc9474; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_dimensiones
    ADD CONSTRAINT "D52be5ea6e9dda03c2e5c101fafc9474" FOREIGN KEY (instrumento_id) REFERENCES cuestionarios_360_instrumentos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3267 (class 2606 OID 24535)
-- Name: D652e4259b0396823b1fe60ad96224df; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas
    ADD CONSTRAINT "D652e4259b0396823b1fe60ad96224df" FOREIGN KEY (instrumento_id) REFERENCES cuestionarios_360_instrumentos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3273 (class 2606 OID 24570)
-- Name: D6600607934e55582d93dfd3fb2873d6; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT "D6600607934e55582d93dfd3fb2873d6" FOREIGN KEY (instrumento_id) REFERENCES cuestionarios_360_instrumentos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3266 (class 2606 OID 24530)
-- Name: D6a2cd0f8010962fb15c44f1dcf065b3; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas
    ADD CONSTRAINT "D6a2cd0f8010962fb15c44f1dcf065b3" FOREIGN KEY (dimension_id) REFERENCES cuestionarios_360_dimensiones(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3247 (class 2606 OID 16725)
-- Name: D785acf4fc38d829f9524ee618911122; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_streaming
    ADD CONSTRAINT "D785acf4fc38d829f9524ee618911122" FOREIGN KEY (colaborador_id) REFERENCES colaboradores_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3279 (class 2606 OID 24606)
-- Name: D7a66978db70a3136552a2bc796b7902; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes
    ADD CONSTRAINT "D7a66978db70a3136552a2bc796b7902" FOREIGN KEY (instrumento_id) REFERENCES cuestionarios_360_instrumentos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3263 (class 2606 OID 24512)
-- Name: D7e370df6069cfd2088c0804160bead3; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_variables
    ADD CONSTRAINT "D7e370df6069cfd2088c0804160bead3" FOREIGN KEY (dimension_id) REFERENCES cuestionarios_360_dimensiones(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3272 (class 2606 OID 24565)
-- Name: D80370afe1794b637efa1cafc6f5e97f; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT "D80370afe1794b637efa1cafc6f5e97f" FOREIGN KEY (evaluado_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3264 (class 2606 OID 24517)
-- Name: D97fac7449934f8003820a149573f57a; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_variables
    ADD CONSTRAINT "D97fac7449934f8003820a149573f57a" FOREIGN KEY (instrumento_id) REFERENCES cuestionarios_360_instrumentos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3271 (class 2606 OID 24560)
-- Name: a0486e25d01d8f0ce78f9996546b8625; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT a0486e25d01d8f0ce78f9996546b8625 FOREIGN KEY (colaborador_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3278 (class 2606 OID 24601)
-- Name: a37ac356854f51347377f9809d765e2c; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes
    ADD CONSTRAINT a37ac356854f51347377f9809d765e2c FOREIGN KEY (evaluado_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3227 (class 2606 OID 16730)
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3225 (class 2606 OID 16735)
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3226 (class 2606 OID 16740)
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3230 (class 2606 OID 16745)
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3228 (class 2606 OID 16750)
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3229 (class 2606 OID 16755)
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3231 (class 2606 OID 16760)
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3270 (class 2606 OID 24554)
-- Name: c_pregunta_id_7dda81ebda38200_fk_cuestionarios_360_preguntas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_respuestas
    ADD CONSTRAINT c_pregunta_id_7dda81ebda38200_fk_cuestionarios_360_preguntas_id FOREIGN KEY (pregunta_id) REFERENCES cuestionarios_360_preguntas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3258 (class 2606 OID 24481)
-- Name: co_id_id_36d9330ac1e757ee_fk_colaboradores_360_colaboradores_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_metricas
    ADD CONSTRAINT co_id_id_36d9330ac1e757ee_fk_colaboradores_360_colaboradores_id FOREIGN KEY (id_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3257 (class 2606 OID 24476)
-- Name: co_id_id_4690d6507c430e6c_fk_colaboradores_360_colaboradores_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_datos
    ADD CONSTRAINT co_id_id_4690d6507c430e6c_fk_colaboradores_360_colaboradores_id FOREIGN KEY (id_id) REFERENCES colaboradores_360_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3232 (class 2606 OID 16765)
-- Name: cola_proyecto_id_1f3bd0fa34f9fda9_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_colaboradores
    ADD CONSTRAINT cola_proyecto_id_1f3bd0fa34f9fda9_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3256 (class 2606 OID 24470)
-- Name: cola_proyecto_id_34b532ceea2c7521_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_colaboradores
    ADD CONSTRAINT cola_proyecto_id_34b532ceea2c7521_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3259 (class 2606 OID 24486)
-- Name: cola_proyecto_id_6742655ca2e26a5e_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_360_roles
    ADD CONSTRAINT cola_proyecto_id_6742655ca2e26a5e_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3233 (class 2606 OID 16770)
-- Name: colabo_id_id_51713430ff7285c4_fk_colaboradores_colaboradores_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_datos
    ADD CONSTRAINT colabo_id_id_51713430ff7285c4_fk_colaboradores_colaboradores_id FOREIGN KEY (id_id) REFERENCES colaboradores_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3234 (class 2606 OID 16775)
-- Name: colabor_id_id_cea314978b28132_fk_colaboradores_colaboradores_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY colaboradores_metricas
    ADD CONSTRAINT colabor_id_id_cea314978b28132_fk_colaboradores_colaboradores_id FOREIGN KEY (id_id) REFERENCES colaboradores_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3237 (class 2606 OID 16780)
-- Name: cue_proyectos_id_23e3516aab6d532e_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos_usuarios
    ADD CONSTRAINT cue_proyectos_id_23e3516aab6d532e_fk_cuestionarios_proyectos_id FOREIGN KEY (proyectos_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3260 (class 2606 OID 24492)
-- Name: cues_proyecto_id_130ceaf226ad60f9_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_instrumentos
    ADD CONSTRAINT cues_proyecto_id_130ceaf226ad60f9_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3269 (class 2606 OID 24545)
-- Name: cues_proyecto_id_1832d416641bf3f6_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas
    ADD CONSTRAINT cues_proyecto_id_1832d416641bf3f6_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3240 (class 2606 OID 16785)
-- Name: cues_proyecto_id_5cb56e0816518094_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_variables
    ADD CONSTRAINT cues_proyecto_id_5cb56e0816518094_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3262 (class 2606 OID 24505)
-- Name: cues_proyecto_id_6fcc6fb0d53b8c59_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_dimensiones
    ADD CONSTRAINT cues_proyecto_id_6fcc6fb0d53b8c59_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3265 (class 2606 OID 24522)
-- Name: cues_proyecto_id_728f982d472ce700_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_variables
    ADD CONSTRAINT cues_proyecto_id_728f982d472ce700_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3235 (class 2606 OID 16790)
-- Name: cues_variable_id_44005723068181a7_fk_cuestionarios_variables_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_preguntas
    ADD CONSTRAINT cues_variable_id_44005723068181a7_fk_cuestionarios_variables_id FOREIGN KEY (variable_id) REFERENCES cuestionarios_variables(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3239 (class 2606 OID 16795)
-- Name: cuest_pregunta_id_9aadaf08526e444_fk_cuestionarios_preguntas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_respuestas
    ADD CONSTRAINT cuest_pregunta_id_9aadaf08526e444_fk_cuestionarios_preguntas_id FOREIGN KEY (pregunta_id) REFERENCES cuestionarios_preguntas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3236 (class 2606 OID 16800)
-- Name: cuestionari_empresa_id_1b15ead3f9a69e28_fk_usuarios_empresas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos
    ADD CONSTRAINT cuestionari_empresa_id_1b15ead3f9a69e28_fk_usuarios_empresas_id FOREIGN KEY (empresa_id) REFERENCES usuarios_empresas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3238 (class 2606 OID 16805)
-- Name: cuestionarios_proyecto_user_id_76b76fd475e3a81e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_proyectos_usuarios
    ADD CONSTRAINT cuestionarios_proyecto_user_id_76b76fd475e3a81e_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3241 (class 2606 OID 16810)
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3242 (class 2606 OID 16815)
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3274 (class 2606 OID 24575)
-- Name: m_pregunta_id_4014874c2e5b188_fk_cuestionarios_360_preguntas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT m_pregunta_id_4014874c2e5b188_fk_cuestionarios_360_preguntas_id FOREIGN KEY (pregunta_id) REFERENCES cuestionarios_360_preguntas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3246 (class 2606 OID 16820)
-- Name: m_usuario_id_181f6b874c64aa6b_fk_colaboradores_colaboradores_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_srs
    ADD CONSTRAINT m_usuario_id_181f6b874c64aa6b_fk_colaboradores_colaboradores_id FOREIGN KEY (usuario_id) REFERENCES colaboradores_colaboradores(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3248 (class 2606 OID 16825)
-- Name: mens_pregunta_id_4424bb06a25710dc_fk_cuestionarios_preguntas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_streaming
    ADD CONSTRAINT mens_pregunta_id_4424bb06a25710dc_fk_cuestionarios_preguntas_id FOREIGN KEY (pregunta_id) REFERENCES cuestionarios_preguntas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3243 (class 2606 OID 16830)
-- Name: mens_pregunta_id_6d9ab7069f959b03_fk_cuestionarios_preguntas_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_externa
    ADD CONSTRAINT mens_pregunta_id_6d9ab7069f959b03_fk_cuestionarios_preguntas_id FOREIGN KEY (pregunta_id) REFERENCES cuestionarios_preguntas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3249 (class 2606 OID 16835)
-- Name: mens_proyecto_id_1ce6660dd85fe095_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_streaming
    ADD CONSTRAINT mens_proyecto_id_1ce6660dd85fe095_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3245 (class 2606 OID 16840)
-- Name: mens_proyecto_id_52759e3afcc1136e_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_metricasexterna
    ADD CONSTRAINT mens_proyecto_id_52759e3afcc1136e_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3275 (class 2606 OID 24580)
-- Name: mens_proyecto_id_7408fdbcc96facf9_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT mens_proyecto_id_7408fdbcc96facf9_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3244 (class 2606 OID 16845)
-- Name: mensaj_proyecto_id_bfd374c1502866_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_externa
    ADD CONSTRAINT mensaj_proyecto_id_bfd374c1502866_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3276 (class 2606 OID 24585)
-- Name: mensajeria_360_st_red_id_29b6b25f6c76bc6c_fk_redes_360_redes_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY mensajeria_360_streaming
    ADD CONSTRAINT mensajeria_360_st_red_id_29b6b25f6c76bc6c_fk_redes_360_redes_id FOREIGN KEY (red_id) REFERENCES redes_360_redes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3280 (class 2606 OID 24611)
-- Name: rede_proyecto_id_26a23c519b92c329_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY redes_360_redes
    ADD CONSTRAINT rede_proyecto_id_26a23c519b92c329_fk_cuestionarios_proyectos_id FOREIGN KEY (proyecto_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3250 (class 2606 OID 16850)
-- Name: usuarios_empresas_usuario_id_4e1348d12461a6e2_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_empresas
    ADD CONSTRAINT usuarios_empresas_usuario_id_4e1348d12461a6e2_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3251 (class 2606 OID 16855)
-- Name: usuarios_indic_parent_id_21af5db625d6b637_fk_usuarios_indice_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_indice
    ADD CONSTRAINT usuarios_indic_parent_id_21af5db625d6b637_fk_usuarios_indice_id FOREIGN KEY (parent_id) REFERENCES usuarios_indice(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3252 (class 2606 OID 16860)
-- Name: usuarios_indice_usuario_id_1b23dcd40d528274_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_indice
    ADD CONSTRAINT usuarios_indice_usuario_id_1b23dcd40d528274_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3254 (class 2606 OID 16865)
-- Name: usuarios_p_id_id_1f644656d51aa7bd_fk_cuestionarios_proyectos_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_proyectosdatos
    ADD CONSTRAINT usuarios_p_id_id_1f644656d51aa7bd_fk_cuestionarios_proyectos_id FOREIGN KEY (id_id) REFERENCES cuestionarios_proyectos(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3253 (class 2606 OID 16870)
-- Name: usuarios_permisos_id_id_6dbe097e0da53adc_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_permisos
    ADD CONSTRAINT usuarios_permisos_id_id_6dbe097e0da53adc_fk_auth_user_id FOREIGN KEY (id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3255 (class 2606 OID 16875)
-- Name: usuarios_recuperar_usuario_id_57ce66516aa7f6c8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY usuarios_recuperar
    ADD CONSTRAINT usuarios_recuperar_usuario_id_57ce66516aa7f6c8_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3268 (class 2606 OID 24540)
-- Name: variable_id_127c89ac699098cb_fk_cuestionarios_360_variables_id; Type: FK CONSTRAINT; Schema: public; Owner: suidi
--

ALTER TABLE ONLY cuestionarios_360_preguntas
    ADD CONSTRAINT variable_id_127c89ac699098cb_fk_cuestionarios_360_variables_id FOREIGN KEY (variable_id) REFERENCES cuestionarios_360_variables(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3396 (class 0 OID 0)
-- Dependencies: 7
-- Name: public; Type: ACL; Schema: -; Owner: suidi
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM suidi;
GRANT ALL ON SCHEMA public TO suidi;
GRANT ALL ON SCHEMA public TO applicacion_gogo;


--
-- TOC entry 3398 (class 0 OID 0)
-- Dependencies: 173
-- Name: auth_group; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_group FROM PUBLIC;
REVOKE ALL ON TABLE auth_group FROM suidi;
GRANT ALL ON TABLE auth_group TO suidi;
GRANT ALL ON TABLE auth_group TO applicacion_gogo;


--
-- TOC entry 3400 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_group_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_group_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_group_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_group_id_seq TO applicacion_gogo;


--
-- TOC entry 3401 (class 0 OID 0)
-- Dependencies: 175
-- Name: auth_group_permissions; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_group_permissions FROM PUBLIC;
REVOKE ALL ON TABLE auth_group_permissions FROM suidi;
GRANT ALL ON TABLE auth_group_permissions TO suidi;
GRANT ALL ON TABLE auth_group_permissions TO applicacion_gogo;


--
-- TOC entry 3403 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_permissions_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_group_permissions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_group_permissions_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_group_permissions_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_group_permissions_id_seq TO applicacion_gogo;


--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 177
-- Name: auth_permission; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_permission FROM PUBLIC;
REVOKE ALL ON TABLE auth_permission FROM suidi;
GRANT ALL ON TABLE auth_permission TO suidi;
GRANT ALL ON TABLE auth_permission TO applicacion_gogo;


--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_permission_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_permission_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_permission_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_permission_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_permission_id_seq TO applicacion_gogo;


--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 179
-- Name: auth_user; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_user FROM PUBLIC;
REVOKE ALL ON TABLE auth_user FROM suidi;
GRANT ALL ON TABLE auth_user TO suidi;
GRANT ALL ON TABLE auth_user TO applicacion_gogo;


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 180
-- Name: auth_user_groups; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_user_groups FROM PUBLIC;
REVOKE ALL ON TABLE auth_user_groups FROM suidi;
GRANT ALL ON TABLE auth_user_groups TO suidi;
GRANT ALL ON TABLE auth_user_groups TO applicacion_gogo;


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_groups_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_user_groups_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_user_groups_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_user_groups_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_user_groups_id_seq TO applicacion_gogo;


--
-- TOC entry 3412 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_user_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_user_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_user_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_user_id_seq TO applicacion_gogo;


--
-- TOC entry 3413 (class 0 OID 0)
-- Dependencies: 183
-- Name: auth_user_user_permissions; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE auth_user_user_permissions FROM PUBLIC;
REVOKE ALL ON TABLE auth_user_user_permissions FROM suidi;
GRANT ALL ON TABLE auth_user_user_permissions TO suidi;
GRANT ALL ON TABLE auth_user_user_permissions TO applicacion_gogo;


--
-- TOC entry 3415 (class 0 OID 0)
-- Dependencies: 184
-- Name: auth_user_user_permissions_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE auth_user_user_permissions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE auth_user_user_permissions_id_seq FROM suidi;
GRANT ALL ON SEQUENCE auth_user_user_permissions_id_seq TO suidi;
GRANT ALL ON SEQUENCE auth_user_user_permissions_id_seq TO applicacion_gogo;


--
-- TOC entry 3416 (class 0 OID 0)
-- Dependencies: 227
-- Name: colaboradores_360_colaboradores; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_360_colaboradores FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_360_colaboradores FROM suidi;
GRANT ALL ON TABLE colaboradores_360_colaboradores TO suidi;
GRANT ALL ON TABLE colaboradores_360_colaboradores TO applicacion_gogo;


--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 226
-- Name: colaboradores_360_colaboradores_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE colaboradores_360_colaboradores_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE colaboradores_360_colaboradores_id_seq FROM suidi;
GRANT ALL ON SEQUENCE colaboradores_360_colaboradores_id_seq TO suidi;
GRANT ALL ON SEQUENCE colaboradores_360_colaboradores_id_seq TO applicacion_gogo;


--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 228
-- Name: colaboradores_360_datos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_360_datos FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_360_datos FROM suidi;
GRANT ALL ON TABLE colaboradores_360_datos TO suidi;
GRANT ALL ON TABLE colaboradores_360_datos TO applicacion_gogo;


--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 229
-- Name: colaboradores_360_metricas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_360_metricas FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_360_metricas FROM suidi;
GRANT ALL ON TABLE colaboradores_360_metricas TO suidi;
GRANT ALL ON TABLE colaboradores_360_metricas TO applicacion_gogo;


--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 231
-- Name: colaboradores_360_roles; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_360_roles FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_360_roles FROM suidi;
GRANT ALL ON TABLE colaboradores_360_roles TO suidi;
GRANT ALL ON TABLE colaboradores_360_roles TO applicacion_gogo;


--
-- TOC entry 3423 (class 0 OID 0)
-- Dependencies: 230
-- Name: colaboradores_360_roles_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE colaboradores_360_roles_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE colaboradores_360_roles_id_seq FROM suidi;
GRANT ALL ON SEQUENCE colaboradores_360_roles_id_seq TO suidi;
GRANT ALL ON SEQUENCE colaboradores_360_roles_id_seq TO applicacion_gogo;


--
-- TOC entry 3424 (class 0 OID 0)
-- Dependencies: 185
-- Name: colaboradores_colaboradores; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_colaboradores FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_colaboradores FROM suidi;
GRANT ALL ON TABLE colaboradores_colaboradores TO suidi;
GRANT ALL ON TABLE colaboradores_colaboradores TO applicacion_gogo;


--
-- TOC entry 3426 (class 0 OID 0)
-- Dependencies: 186
-- Name: colaboradores_colaboradores_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE colaboradores_colaboradores_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE colaboradores_colaboradores_id_seq FROM suidi;
GRANT ALL ON SEQUENCE colaboradores_colaboradores_id_seq TO suidi;
GRANT ALL ON SEQUENCE colaboradores_colaboradores_id_seq TO applicacion_gogo;


--
-- TOC entry 3427 (class 0 OID 0)
-- Dependencies: 187
-- Name: colaboradores_datos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_datos FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_datos FROM suidi;
GRANT ALL ON TABLE colaboradores_datos TO suidi;
GRANT ALL ON TABLE colaboradores_datos TO applicacion_gogo;


--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 188
-- Name: colaboradores_metricas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE colaboradores_metricas FROM PUBLIC;
REVOKE ALL ON TABLE colaboradores_metricas FROM suidi;
GRANT ALL ON TABLE colaboradores_metricas TO suidi;
GRANT ALL ON TABLE colaboradores_metricas TO applicacion_gogo;


--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 235
-- Name: cuestionarios_360_dimensiones; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_360_dimensiones FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_360_dimensiones FROM suidi;
GRANT ALL ON TABLE cuestionarios_360_dimensiones TO suidi;
GRANT ALL ON TABLE cuestionarios_360_dimensiones TO applicacion_gogo;


--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 234
-- Name: cuestionarios_360_dimensiones_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_360_dimensiones_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_360_dimensiones_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_dimensiones_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_dimensiones_id_seq TO applicacion_gogo;


--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 233
-- Name: cuestionarios_360_instrumentos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_360_instrumentos FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_360_instrumentos FROM suidi;
GRANT ALL ON TABLE cuestionarios_360_instrumentos TO suidi;
GRANT ALL ON TABLE cuestionarios_360_instrumentos TO applicacion_gogo;


--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 232
-- Name: cuestionarios_360_instrumentos_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_360_instrumentos_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_360_instrumentos_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_instrumentos_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_instrumentos_id_seq TO applicacion_gogo;


--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 239
-- Name: cuestionarios_360_preguntas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_360_preguntas FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_360_preguntas FROM suidi;
GRANT ALL ON TABLE cuestionarios_360_preguntas TO suidi;
GRANT ALL ON TABLE cuestionarios_360_preguntas TO applicacion_gogo;


--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 238
-- Name: cuestionarios_360_preguntas_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_360_preguntas_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_360_preguntas_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_preguntas_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_preguntas_id_seq TO applicacion_gogo;


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 241
-- Name: cuestionarios_360_respuestas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_360_respuestas FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_360_respuestas FROM suidi;
GRANT ALL ON TABLE cuestionarios_360_respuestas TO suidi;
GRANT ALL ON TABLE cuestionarios_360_respuestas TO applicacion_gogo;


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 240
-- Name: cuestionarios_360_respuestas_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_360_respuestas_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_360_respuestas_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_respuestas_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_respuestas_id_seq TO applicacion_gogo;


--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 237
-- Name: cuestionarios_360_variables; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_360_variables FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_360_variables FROM suidi;
GRANT ALL ON TABLE cuestionarios_360_variables TO suidi;
GRANT ALL ON TABLE cuestionarios_360_variables TO applicacion_gogo;


--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 236
-- Name: cuestionarios_360_variables_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_360_variables_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_360_variables_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_variables_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_360_variables_id_seq TO applicacion_gogo;


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 189
-- Name: cuestionarios_preguntas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_preguntas FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_preguntas FROM suidi;
GRANT ALL ON TABLE cuestionarios_preguntas TO suidi;
GRANT ALL ON TABLE cuestionarios_preguntas TO applicacion_gogo;


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 190
-- Name: cuestionarios_preguntas_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_preguntas_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_preguntas_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_preguntas_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_preguntas_id_seq TO applicacion_gogo;


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 191
-- Name: cuestionarios_proyectos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_proyectos FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_proyectos FROM suidi;
GRANT ALL ON TABLE cuestionarios_proyectos TO suidi;
GRANT ALL ON TABLE cuestionarios_proyectos TO applicacion_gogo;


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 192
-- Name: cuestionarios_proyectos_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_proyectos_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_proyectos_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_proyectos_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_proyectos_id_seq TO applicacion_gogo;


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 193
-- Name: cuestionarios_proyectos_usuarios; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_proyectos_usuarios FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_proyectos_usuarios FROM suidi;
GRANT ALL ON TABLE cuestionarios_proyectos_usuarios TO suidi;
GRANT ALL ON TABLE cuestionarios_proyectos_usuarios TO applicacion_gogo;


--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 194
-- Name: cuestionarios_proyectos_usuarios_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_proyectos_usuarios_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_proyectos_usuarios_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_proyectos_usuarios_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_proyectos_usuarios_id_seq TO applicacion_gogo;


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 195
-- Name: cuestionarios_respuestas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_respuestas FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_respuestas FROM suidi;
GRANT ALL ON TABLE cuestionarios_respuestas TO suidi;
GRANT ALL ON TABLE cuestionarios_respuestas TO applicacion_gogo;


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 196
-- Name: cuestionarios_respuestas_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_respuestas_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_respuestas_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_respuestas_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_respuestas_id_seq TO applicacion_gogo;


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 197
-- Name: cuestionarios_variables; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE cuestionarios_variables FROM PUBLIC;
REVOKE ALL ON TABLE cuestionarios_variables FROM suidi;
GRANT ALL ON TABLE cuestionarios_variables TO suidi;
GRANT ALL ON TABLE cuestionarios_variables TO applicacion_gogo;


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 198
-- Name: cuestionarios_variables_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE cuestionarios_variables_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cuestionarios_variables_id_seq FROM suidi;
GRANT ALL ON SEQUENCE cuestionarios_variables_id_seq TO suidi;
GRANT ALL ON SEQUENCE cuestionarios_variables_id_seq TO applicacion_gogo;


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 199
-- Name: django_admin_log; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE django_admin_log FROM PUBLIC;
REVOKE ALL ON TABLE django_admin_log FROM suidi;
GRANT ALL ON TABLE django_admin_log TO suidi;
GRANT ALL ON TABLE django_admin_log TO applicacion_gogo;


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 200
-- Name: django_admin_log_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE django_admin_log_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE django_admin_log_id_seq FROM suidi;
GRANT ALL ON SEQUENCE django_admin_log_id_seq TO suidi;
GRANT ALL ON SEQUENCE django_admin_log_id_seq TO applicacion_gogo;


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 201
-- Name: django_content_type; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE django_content_type FROM PUBLIC;
REVOKE ALL ON TABLE django_content_type FROM suidi;
GRANT ALL ON TABLE django_content_type TO suidi;
GRANT ALL ON TABLE django_content_type TO applicacion_gogo;


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_content_type_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE django_content_type_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE django_content_type_id_seq FROM suidi;
GRANT ALL ON SEQUENCE django_content_type_id_seq TO suidi;
GRANT ALL ON SEQUENCE django_content_type_id_seq TO applicacion_gogo;


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 203
-- Name: django_migrations; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE django_migrations FROM PUBLIC;
REVOKE ALL ON TABLE django_migrations FROM suidi;
GRANT ALL ON TABLE django_migrations TO suidi;
GRANT ALL ON TABLE django_migrations TO applicacion_gogo;


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 204
-- Name: django_migrations_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE django_migrations_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE django_migrations_id_seq FROM suidi;
GRANT ALL ON SEQUENCE django_migrations_id_seq TO suidi;
GRANT ALL ON SEQUENCE django_migrations_id_seq TO applicacion_gogo;


--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 205
-- Name: django_session; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE django_session FROM PUBLIC;
REVOKE ALL ON TABLE django_session FROM suidi;
GRANT ALL ON TABLE django_session TO suidi;
GRANT ALL ON TABLE django_session TO applicacion_gogo;


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 243
-- Name: mensajeria_360_streaming; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE mensajeria_360_streaming FROM PUBLIC;
REVOKE ALL ON TABLE mensajeria_360_streaming FROM suidi;
GRANT ALL ON TABLE mensajeria_360_streaming TO suidi;
GRANT ALL ON TABLE mensajeria_360_streaming TO applicacion_gogo;


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 242
-- Name: mensajeria_360_streaming_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE mensajeria_360_streaming_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mensajeria_360_streaming_id_seq FROM suidi;
GRANT ALL ON SEQUENCE mensajeria_360_streaming_id_seq TO suidi;
GRANT ALL ON SEQUENCE mensajeria_360_streaming_id_seq TO applicacion_gogo;


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 206
-- Name: mensajeria_externa; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE mensajeria_externa FROM PUBLIC;
REVOKE ALL ON TABLE mensajeria_externa FROM suidi;
GRANT ALL ON TABLE mensajeria_externa TO suidi;
GRANT ALL ON TABLE mensajeria_externa TO applicacion_gogo;


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 207
-- Name: mensajeria_externa_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE mensajeria_externa_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mensajeria_externa_id_seq FROM suidi;
GRANT ALL ON SEQUENCE mensajeria_externa_id_seq TO suidi;
GRANT ALL ON SEQUENCE mensajeria_externa_id_seq TO applicacion_gogo;


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 208
-- Name: mensajeria_metricasexterna; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE mensajeria_metricasexterna FROM PUBLIC;
REVOKE ALL ON TABLE mensajeria_metricasexterna FROM suidi;
GRANT ALL ON TABLE mensajeria_metricasexterna TO suidi;
GRANT ALL ON TABLE mensajeria_metricasexterna TO applicacion_gogo;


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 209
-- Name: mensajeria_metricasexterna_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE mensajeria_metricasexterna_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mensajeria_metricasexterna_id_seq FROM suidi;
GRANT ALL ON SEQUENCE mensajeria_metricasexterna_id_seq TO suidi;
GRANT ALL ON SEQUENCE mensajeria_metricasexterna_id_seq TO applicacion_gogo;


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 210
-- Name: mensajeria_srs; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE mensajeria_srs FROM PUBLIC;
REVOKE ALL ON TABLE mensajeria_srs FROM suidi;
GRANT ALL ON TABLE mensajeria_srs TO suidi;
GRANT ALL ON TABLE mensajeria_srs TO applicacion_gogo;


--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 211
-- Name: mensajeria_srs_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE mensajeria_srs_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mensajeria_srs_id_seq FROM suidi;
GRANT ALL ON SEQUENCE mensajeria_srs_id_seq TO suidi;
GRANT ALL ON SEQUENCE mensajeria_srs_id_seq TO applicacion_gogo;


--
-- TOC entry 3481 (class 0 OID 0)
-- Dependencies: 212
-- Name: mensajeria_streaming; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE mensajeria_streaming FROM PUBLIC;
REVOKE ALL ON TABLE mensajeria_streaming FROM suidi;
GRANT ALL ON TABLE mensajeria_streaming TO suidi;
GRANT ALL ON TABLE mensajeria_streaming TO applicacion_gogo;


--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 213
-- Name: mensajeria_streaming_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE mensajeria_streaming_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mensajeria_streaming_id_seq FROM suidi;
GRANT ALL ON SEQUENCE mensajeria_streaming_id_seq TO suidi;
GRANT ALL ON SEQUENCE mensajeria_streaming_id_seq TO applicacion_gogo;


--
-- TOC entry 3484 (class 0 OID 0)
-- Dependencies: 245
-- Name: redes_360_redes; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE redes_360_redes FROM PUBLIC;
REVOKE ALL ON TABLE redes_360_redes FROM suidi;
GRANT ALL ON TABLE redes_360_redes TO suidi;
GRANT ALL ON TABLE redes_360_redes TO applicacion_gogo;


--
-- TOC entry 3486 (class 0 OID 0)
-- Dependencies: 244
-- Name: redes_360_redes_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE redes_360_redes_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE redes_360_redes_id_seq FROM suidi;
GRANT ALL ON SEQUENCE redes_360_redes_id_seq TO suidi;
GRANT ALL ON SEQUENCE redes_360_redes_id_seq TO applicacion_gogo;


--
-- TOC entry 3487 (class 0 OID 0)
-- Dependencies: 214
-- Name: usuarios_empresas; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_empresas FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_empresas FROM suidi;
GRANT ALL ON TABLE usuarios_empresas TO suidi;
GRANT ALL ON TABLE usuarios_empresas TO applicacion_gogo;


--
-- TOC entry 3489 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuarios_empresas_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE usuarios_empresas_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usuarios_empresas_id_seq FROM suidi;
GRANT ALL ON SEQUENCE usuarios_empresas_id_seq TO suidi;
GRANT ALL ON SEQUENCE usuarios_empresas_id_seq TO applicacion_gogo;


--
-- TOC entry 3490 (class 0 OID 0)
-- Dependencies: 216
-- Name: usuarios_errores; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_errores FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_errores FROM suidi;
GRANT ALL ON TABLE usuarios_errores TO suidi;
GRANT ALL ON TABLE usuarios_errores TO applicacion_gogo;


--
-- TOC entry 3492 (class 0 OID 0)
-- Dependencies: 217
-- Name: usuarios_errores_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE usuarios_errores_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usuarios_errores_id_seq FROM suidi;
GRANT ALL ON SEQUENCE usuarios_errores_id_seq TO suidi;
GRANT ALL ON SEQUENCE usuarios_errores_id_seq TO applicacion_gogo;


--
-- TOC entry 3493 (class 0 OID 0)
-- Dependencies: 218
-- Name: usuarios_indice; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_indice FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_indice FROM suidi;
GRANT ALL ON TABLE usuarios_indice TO suidi;
GRANT ALL ON TABLE usuarios_indice TO applicacion_gogo;


--
-- TOC entry 3495 (class 0 OID 0)
-- Dependencies: 219
-- Name: usuarios_indice_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE usuarios_indice_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usuarios_indice_id_seq FROM suidi;
GRANT ALL ON SEQUENCE usuarios_indice_id_seq TO suidi;
GRANT ALL ON SEQUENCE usuarios_indice_id_seq TO applicacion_gogo;


--
-- TOC entry 3496 (class 0 OID 0)
-- Dependencies: 220
-- Name: usuarios_logs; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_logs FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_logs FROM suidi;
GRANT ALL ON TABLE usuarios_logs TO suidi;
GRANT ALL ON TABLE usuarios_logs TO applicacion_gogo;


--
-- TOC entry 3498 (class 0 OID 0)
-- Dependencies: 221
-- Name: usuarios_logs_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE usuarios_logs_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usuarios_logs_id_seq FROM suidi;
GRANT ALL ON SEQUENCE usuarios_logs_id_seq TO suidi;
GRANT ALL ON SEQUENCE usuarios_logs_id_seq TO applicacion_gogo;


--
-- TOC entry 3499 (class 0 OID 0)
-- Dependencies: 222
-- Name: usuarios_permisos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_permisos FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_permisos FROM suidi;
GRANT ALL ON TABLE usuarios_permisos TO suidi;
GRANT ALL ON TABLE usuarios_permisos TO applicacion_gogo;


--
-- TOC entry 3500 (class 0 OID 0)
-- Dependencies: 223
-- Name: usuarios_proyectosdatos; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_proyectosdatos FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_proyectosdatos FROM suidi;
GRANT ALL ON TABLE usuarios_proyectosdatos TO suidi;
GRANT ALL ON TABLE usuarios_proyectosdatos TO applicacion_gogo;


--
-- TOC entry 3501 (class 0 OID 0)
-- Dependencies: 224
-- Name: usuarios_recuperar; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON TABLE usuarios_recuperar FROM PUBLIC;
REVOKE ALL ON TABLE usuarios_recuperar FROM suidi;
GRANT ALL ON TABLE usuarios_recuperar TO suidi;
GRANT ALL ON TABLE usuarios_recuperar TO applicacion_gogo;


--
-- TOC entry 3503 (class 0 OID 0)
-- Dependencies: 225
-- Name: usuarios_recuperar_id_seq; Type: ACL; Schema: public; Owner: suidi
--

REVOKE ALL ON SEQUENCE usuarios_recuperar_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usuarios_recuperar_id_seq FROM suidi;
GRANT ALL ON SEQUENCE usuarios_recuperar_id_seq TO suidi;
GRANT ALL ON SEQUENCE usuarios_recuperar_id_seq TO applicacion_gogo;


--
-- TOC entry 1789 (class 826 OID 17603)
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON SEQUENCES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON SEQUENCES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public GRANT ALL ON SEQUENCES  TO applicacion_gogo;


--
-- TOC entry 1793 (class 826 OID 17607)
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: -; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON SEQUENCES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON SEQUENCES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON SEQUENCES  TO suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON SEQUENCES  TO applicacion_gogo;


--
-- TOC entry 1795 (class 826 OID 17597)
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: -; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON TYPES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON TYPES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON TYPES  TO suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON TYPES  TO applicacion_gogo;


--
-- TOC entry 1791 (class 826 OID 17605)
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: public; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON TYPES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON TYPES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public GRANT ALL ON TYPES  TO applicacion_gogo;


--
-- TOC entry 1794 (class 826 OID 17596)
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: -; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON FUNCTIONS  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON FUNCTIONS  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON FUNCTIONS  TO suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON FUNCTIONS  TO applicacion_gogo;


--
-- TOC entry 1790 (class 826 OID 17604)
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON FUNCTIONS  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON FUNCTIONS  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public GRANT ALL ON FUNCTIONS  TO applicacion_gogo;


--
-- TOC entry 1788 (class 826 OID 17602)
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON TABLES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public REVOKE ALL ON TABLES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi IN SCHEMA public GRANT ALL ON TABLES  TO applicacion_gogo;


--
-- TOC entry 1792 (class 826 OID 17606)
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: suidi
--

ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON TABLES  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi REVOKE ALL ON TABLES  FROM suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON TABLES  TO suidi;
ALTER DEFAULT PRIVILEGES FOR ROLE suidi GRANT ALL ON TABLES  TO applicacion_gogo;


-- Completed on 2016-06-14 09:19:27 COT

--
-- PostgreSQL database dump complete
--

