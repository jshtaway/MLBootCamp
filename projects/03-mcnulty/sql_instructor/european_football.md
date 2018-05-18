# European Football

The ultimate Soccer database for data analysis and machine learning!

Notes, tips, and SQL commands for importing the european football data set into PostgreSQL.

This database is in sqlite format. There may be a way to import directly into PostgreSQL, however another way is to dump each file to a csv first and then import as normal. This code requires python 3 to handle text encoding.

```python
import sqlite3
import pandas as pd
con = sqlite3.connect('./european_football/database.sqlite')

table_list = ['Country', 'League', 'Match', 
              'Player', 'Player_Attributes',
              'Team', 'Team_Attributes']

for table in table_list:
    csv_name = 'european_football/' + table.lower() + '.csv'
    tbl = pd.read_sql('SELECT * FROM {}'.format(table), con)
    tbl.to_csv(csv_name, index=False, encoding="utf-8")
```

## Countries

```sql
CREATE TABLE country (
    id      numeric,
    name    varchar);

COPY country
FROM '/home/ubuntu/european_football/country.csv'
DELIMITER ','
CSV HEADER;
```

## Leagues

```sql
CREATE TABLE league (
    id            numeric,
    country_id    numeric,
    name          varchar);

COPY league
FROM '/home/ubuntu/european_football/league.csv'
DELIMITER ','
CSV HEADER;
```

## Matches

```sql
CREATE TABLE match (
    id                  numeric,
    country_id          numeric,
    league_id           numeric,
    season              varchar,
    stage               numeric,
    date_               varchar,
    match_api_id        numeric,
    home_team_api_id    numeric,
    away_team_api_id    numeric,
    home_team_goal      numeric,
    away_team_goal      numeric,
    home_player_X1      numeric,
    home_player_X2      numeric,
    home_player_X3      numeric,
    home_player_X4      numeric,
    home_player_X5      numeric,
    home_player_X6      numeric,
    home_player_X7      numeric,
    home_player_X8      numeric,
    home_player_X9      numeric,
    home_player_X10     numeric,
    home_player_X11     numeric,
    away_player_X1      numeric,
    away_player_X2      numeric,
    away_player_X3      numeric,
    away_player_X4      numeric,
    away_player_X5      numeric,
    away_player_X6      numeric,
    away_player_X7      numeric,
    away_player_X8      numeric,
    away_player_X9      numeric,
    away_player_X10     numeric,
    away_player_X11     numeric,
    home_player_Y1      numeric,
    home_player_Y2      numeric,
    home_player_Y3      numeric,
    home_player_Y4      numeric,
    home_player_Y5      numeric,
    home_player_Y6      numeric,
    home_player_Y7      numeric,
    home_player_Y8      numeric,
    home_player_Y9      numeric,
    home_player_Y10     numeric,
    home_player_Y11     numeric,
    away_player_Y1      numeric,
    away_player_Y2      numeric,
    away_player_Y3      numeric,
    away_player_Y4      numeric,
    away_player_Y5      numeric,
    away_player_Y6      numeric,
    away_player_Y7      numeric,
    away_player_Y8      numeric,
    away_player_Y9      numeric,
    away_player_Y10     numeric,
    away_player_Y11     numeric,
    home_player_1       numeric,
    home_player_2       numeric,
    home_player_3       numeric,
    home_player_4       numeric,
    home_player_5       numeric,
    home_player_6       numeric,
    home_player_7       numeric,
    home_player_8       numeric,
    home_player_9       numeric,
    home_player_10      numeric,
    home_player_11      numeric,
    away_player_1       numeric,
    away_player_2       numeric,
    away_player_3       numeric,
    away_player_4       numeric,
    away_player_5       numeric,
    away_player_6       numeric,
    away_player_7       numeric,
    away_player_8       numeric,
    away_player_9       numeric,
    away_player_10      numeric,
    away_player_11      numeric,
    goal                varchar,
    shoton              varchar,
    shotoff             varchar,
    foulcommit          varchar,
    card                varchar,
    cross_              varchar,
    corner              varchar,
    possession          varchar,
    B365H               numeric,
    B365D               numeric,
    B365A               numeric,
    BWH                 numeric,
    BWD                 numeric,
    BWA                 numeric,
    IWH                 numeric,
    IWD                 numeric,
    IWA                 numeric,
    LBH                 numeric,
    LBD                 numeric,
    LBA                 numeric,
    PSH                 numeric,
    PSD                 numeric,
    PSA                 numeric,
    WHH                 numeric,
    WHD                 numeric,
    WHA                 numeric,
    SJH                 numeric,
    SJD                 numeric,
    SJA                 numeric,
    VCH                 numeric,
    VCD                 numeric,
    VCA                 numeric,
    GBH                 numeric,
    GBD                 numeric,
    GBA                 numeric,
    BSH                 numeric,
    BSD                 numeric,
    BSA                 numeric);

COPY match
FROM '/home/ubuntu/european_football/match.csv'
DELIMITER ','
CSV HEADER;
```

## Player

```sql
CREATE TABLE player (
    id                    numeric,
    player_api_id         numeric,
    player_name           varchar,
    player_fifa_api_id    numeric,
    birthday              varchar,
    height                numeric,
    weight                numeric);

COPY player
FROM '/home/ubuntu/european_football/player.csv'
DELIMITER ','
CSV HEADER;
```

## Player attributes

```sql
CREATE TABLE player_attributes (
    id                     numeric,
    player_fifa_api_id     numeric,
    player_api_id          numeric,
    date_                  varchar,
    overall_rating         numeric,
    potential              numeric,
    preferred_foot         varchar,
    attacking_work_rate    varchar,
    defensive_work_rate    varchar,
    crossing               numeric,
    finishing              numeric,
    heading_accuracy       numeric,
    short_passing          numeric,
    volleys                numeric,
    dribbling              numeric,
    curve                  numeric,
    free_kick_accuracy     numeric,
    long_passing           numeric,
    ball_control           numeric,
    acceleration           numeric,
    sprint_speed           numeric,
    agility                numeric,
    reactions              numeric,
    balance                numeric,
    shot_power             numeric,
    jumping                numeric,
    stamina                numeric,
    strength               numeric,
    long_shots             numeric,
    aggression             numeric,
    interceptions          numeric,
    positioning            numeric,
    vision                 numeric,
    penalties              numeric,
    marking                numeric,
    standing_tackle        numeric,
    sliding_tackle         numeric,
    gk_diving              numeric,
    gk_handling            numeric,
    gk_kicking             numeric,
    gk_positioning         numeric,
    gk_reflexes            numeric);

COPY player_attributes
FROM '/home/ubuntu/european_football/player_attributes.csv'
DELIMITER ','
CSV HEADER;
```