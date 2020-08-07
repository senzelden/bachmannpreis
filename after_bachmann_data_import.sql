-- CREATE TABLE perlentaucher (
--     author_id INTEGER,
--     book_title VARCHAR(200),
--     publisher VARCHAR(100),
--     release_year INTEGER,
--     perlentaucher_url VARCHAR(200),
--
--     FOREIGN KEY (author_id)
--         REFERENCES authors ON DELETE CASCADE
-- );
--
-- \COPY perlentaucher FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/perlentaucher_updated.csv' DELIMITER ',' CSV HEADER;
--
--
-- CREATE TABLE goodreads (
--     author_id INTEGER,
--     genre VARCHAR(100),
--     total_publications INTEGER,
--     followers INTEGER,
--     average_rating REAL,
--     ratings_count INTEGER,
--
--     FOREIGN KEY (author_id)
--         REFERENCES authors ON DELETE CASCADE
-- );
--
-- \COPY goodreads FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/goodreads_final.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE worldcat (
    author_id INTEGER,
    total_subject_results INTEGER,

    FOREIGN KEY (author_id)
        REFERENCES authors ON DELETE CASCADE
);

\COPY worldcat FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/worldcat_final.csv' DELIMITER ',' CSV HEADER;