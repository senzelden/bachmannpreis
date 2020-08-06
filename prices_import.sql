--CREATE TABLE prices (
--    price_id SERIAL PRIMARY KEY NOT NULL,
--    price_title VARCHAR(200) NOT NULL
--);
--
--\COPY prices FROM '/home/denniss/Desktop/Coding/bachmann_data/prices_names.csv' DELIMITER ',' CSV HEADER;

--CREATE TABLE price_money (
--    price_id INTEGER NOT NULL,
--    price_money INTEGER NOT NULL,
--    currency VARCHAR(50) NOT NULL,
--    price_money_start DATE NOT NULL,
--
--    FOREIGN KEY (price_id)
--        REFERENCES prices ON DELETE CASCADE
--);
--
--\COPY price_money FROM '/home/denniss/Desktop/Coding/bachmann_data/price_money.csv' DELIMITER ',' CSV HEADER;
--
CREATE TABLE results (
    text_id INTEGER,
    price_id INTEGER,

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE,
    FOREIGN KEY (price_id)
        REFERENCES prices ON DELETE CASCADE
);

\COPY results FROM '/home/denniss/Desktop/Coding/bachmann_data/results.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE authors_cities (
    text_id INTEGER NOT NULL,
    author_city VARCHAR(200),

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY authors_cities FROM '/home/denniss/Desktop/Coding/bachmann_data/cities.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE authors_countries (
    text_id INTEGER NOT NULL,
    author_country VARCHAR(200),
    author_country_detail VARCHAR(100),

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY authors_countries FROM '/home/denniss/Desktop/Coding/bachmann_data/countries.csv' DELIMITER ',' CSV HEADER;