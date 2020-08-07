CREATE TABLE cities_geodata (
    city_id INTEGER PRIMARY KEY,
    city_name VARCHAR(100),
    lat REAL,
    lon REAL,
    distance_to_klagenfurt REAL
);

\COPY cities_geodata FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/cities_geodata.csv' DELIMITER ',' CSV HEADER;