CREATE TABLE cities_geodata (
    city_id INTEGER PRIMARY KEY,
    city_name VARCHAR(100),
    lat REAL,
    lon REAL,
    total_authors INTEGER
);

\COPY cities_geodata FROM '/home/denniss/Desktop/Coding/bachmann_data/cities_geodata.csv' DELIMITER ',' CSV HEADER;