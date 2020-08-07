CREATE TABLE texts (
    text_id SERIAL PRIMARY KEY NOT NULL,
    author_id INTEGER NOT NULL,
    text_title VARCHAR(300),
    date_participation DATE,
    invited_by INTEGER,
    on_shortlist BOOLEAN,
    font VARCHAR(100),
    reading_order INTEGER,
    day_reading VARCHAR(20),
    reading_context VARCHAR(20),
    total_days_reading INTEGER,

    FOREIGN KEY(author_id)
        REFERENCES authors ON DELETE CASCADE,
    FOREIGN KEY (invited_by)
        REFERENCES critics
);

\COPY texts FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/texts_updated.csv' DELIMITER ',' CSV HEADER;