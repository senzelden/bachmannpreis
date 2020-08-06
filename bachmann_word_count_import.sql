CREATE TABLE word_count (
    word_id INTEGER PRIMARY KEY,
    word VARCHAR(100),
    count INTEGER
);

\COPY word_count FROM '/home/denniss/Desktop/Coding/bachmann_data/word_count.csv' DELIMITER ',' CSV HEADER;