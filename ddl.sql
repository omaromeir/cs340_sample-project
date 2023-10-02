CREATE TABLE public.movies (
    id integer NOT NULL,
    title text,
    original_language character(2),
    runtime character varying(10),
    revenue numeric,
    genre character varying(30),
    release_date character varying(30),
    production_country character varying(100),
    dir_id integer,
    vote_average real,
    vote_count integer,
    production_company text,
    primary key(id)
);

COPY movies
FROM '/movies_sample.tsv'
DELIMITER '|'
CSV HEADER;