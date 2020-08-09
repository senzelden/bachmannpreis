-- CREATE TABLE cities_geodata (
--     city_id INTEGER PRIMARY KEY,
--     city_name VARCHAR(100),
--     lat REAL,
--     lon REAL,
--     distance_to_klagenfurt REAL
-- );
--
-- \COPY cities_geodata FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/cities_geodata.csv' DELIMITER ',' CSV HEADER;
--
--
-- CREATE TABLE authors_cities (
--     text_city_mapper_id INTEGER PRIMARY KEY,
--     text_id INTEGER,
--     city_name VARCHAR(200),
--     city_id INTEGER,
--
--     FOREIGN KEY (text_id)
--         REFERENCES texts,
--     FOREIGN KEY (city_id)
--         REFERENCES cities_geodata
-- );
--
-- \COPY authors_cities FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/cities_updated.csv' DELIMITER ',' CSV HEADER;


-- CREATE TABLE countries (
--     country_id INTEGER PRIMARY KEY,
--     country_name VARCHAR(200)
-- );
--
-- \COPY countries FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/unique_countries.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE authors_countries (
    text_country_mapper_id INTEGER PRIMARY KEY,
    text_id INTEGER,
    author_country VARCHAR(200),
    country_detail VARCHAR(100),
    country_id INTEGER,

    FOREIGN KEY (text_id)
        REFERENCES texts,
    FOREIGN KEY (country_id)
        REFERENCES countries
);

\COPY authors_countries FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/countries_updated.csv' DELIMITER ',' CSV HEADER;