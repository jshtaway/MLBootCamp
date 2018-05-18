# The Simpson's Data

This dataset contains the characters, locations, episode details, and script lines for approximately 600 Simpsons episodes, dating back to 1989.

## Characters

Contains character names and a character id

```sql
CREATE TABLE characters (
    id                 numeric,
    name               varchar,
    normalized_name    varchar,
    gender             varchar);

COPY characters
FROM '/home/ubuntu/the_simpsons/simpsons_characters.csv'
DELIMITER ','
CSV HEADER;
```

## Episodes

Contains metadata related to each episode.

There are some issues with quote termination that will need to be fixed by the student prior to importing with SQL.

```sql
CREATE TABLE episodes (
    id                        numeric,
    title                     varchar,
    original_air_date         varchar,
    production_code           varchar,
    season                    numeric,
    number_in_season          numeric,
    number_in_series          numeric,
    us_viewers_in_millions    numeric,
    views                     numeric,
    imdb_rating               numeric,
    imdb_votes                numeric,
    image_url                 varchar,
    video_url                 varchar);

COPY episodes
FROM '/home/ubuntu/the_simpsons/simpsons_episodes.csv'
DELIMITER ','
CSV HEADER;
```

## Locations

Contains locations and a location id.

```sql
CREATE TABLE locations (
    id                 numeric,
    name               varchar,
    normalized_name    varchar);

COPY locations
FROM '/home/ubuntu/the_simpsons/simpsons_locations.csv'
DELIMITER ','
CSV HEADER;
```

## Script lines

Contains the text spoken during each episode (including details about which character said it and where).

There are some issues with number of columns per line that will need to be fixed by the student prior to importing with SQL.

```sql
CREATE TABLE script_lines (
    id              numeric,
    episode_id      numeric,
    number_         numeric,
    raw_text        varchar,
    timestamp_in_ms integer,
    speaking_line   varchar,
    character_id    integer,
    location_id     integer);

COPY script_lines
FROM '/home/ubuntu/the_simpsons/simpsons_script_lines.csv'
DELIMITER ','
CSV HEADER;
```