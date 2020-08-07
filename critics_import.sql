CREATE TABLE critics (
   critic_id SERIAL PRIMARY KEY NOT NULL,
   critic_first_name VARCHAR(100) NOT NULL,
   critic_middle_name VARCHAR(100),
   critic_last_name VARCHAR(100),
   critic_birth_place VARCHAR(100),
   critic_birth_date DATE,
   critic_gender VARCHAR(20),
   critic_country VARCHAR(200),
   works_as_critic BOOLEAN,
   is_literary_scholar BOOLEAN,
   is_writer BOOLEAN
);

\COPY critics FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/critics_updated.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE critics_participation (
    year_participation INTEGER,
    critic_id INTEGER NOT NULL,
    critic_living_place VARCHAR(200),
    is_chairman BOOLEAN,
    got_sick BOOLEAN,

    FOREIGN KEY (critic_id)
        REFERENCES critics ON DELETE CASCADE
);

\COPY critics_participation FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/critics_participations_all.csv' DELIMITER ',' CSV HEADER;