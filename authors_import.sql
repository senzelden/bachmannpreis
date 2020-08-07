CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY NOT NULL,
    author_first_name VARCHAR(100) NOT NULL,
    author_middle_name VARCHAR(100),
    author_last_name VARCHAR(100),
    author_birth_date DATE,
    author_birth_place VARCHAR(100),
    author_gender VARCHAR(20),
    author_has_wikipedia BOOLEAN,
    author_website VARCHAR(200),
    author_from_literaturinstitut VARCHAR(100),
    author_has_phd BOOLEAN
);

\COPY authors FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/authors_final.csv' DELIMITER ',' CSV HEADER;