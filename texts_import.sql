CREATE TABLE texts (
    text_id SERIAL PRIMARY KEY NOT NULL,
    text_title VARCHAR(300),
    author_id INTEGER NOT NULL,
    date_participation DATE,
    day_reading VARCHAR(20),
    invited_by INTEGER,
    is_performance BOOLEAN,
    on_shortlist BOOLEAN,
    discussion_summary TEXT,

    FOREIGN KEY(author_id)
        REFERENCES authors ON DELETE CASCADE,
    FOREIGN KEY (invited_by)
        REFERENCES critics
);

\COPY texts FROM '/home/denniss/Desktop/Coding/bachmann_data/texts.csv' DELIMITER ',' CSV HEADER;