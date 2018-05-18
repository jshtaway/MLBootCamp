# Professional Hockey

Notes, tips, and SQL commands for importing the professional hockey data set into PostgreSQL.

The Hockey Database is a collection of historical statistics from men's professional hockey teams in North America.

## Abbreviations

Abbreviations used in Teams and SeriesPost tables

```sql
CREATE TABLE abbrev (
    Type        varchar,
    Code        varchar,
    Fullname    varchar);

COPY abbrev
FROM '/home/ubuntu/professional_hockey/abbrev.csv'
DELIMITER ','
CSV HEADER;
```

## Coaches awards

Coaches awards, trophies, postseason all-star teams

```sql
CREATE TABLE coaches_awards (
    coachID    varchar,
    award      varchar,
    year       numeric,
    lgID       varchar,
    note       numeric);

COPY coaches_awards
FROM '/home/ubuntu/professional_hockey/AwardsCoaches.csv'
DELIMITER ','
CSV HEADER;

```

## Players awards

Player awards, trophies, postseason all-star teams

A number of the rows are missing a comma at the end.

```python
import shutil

with open('AwardsPlayers.csv', 'r') as fh:
    lines = fh.readlines()

shutil.copy('AwardsPlayers.csv', 'AwardsPlayers.bkup')

# split the lines and remove the extras
lines = [x.strip().split(',') for x in lines]
num_fields = max([len(x) for x in lines])

for x in range(len(lines)):
    if len(lines[x]) < num_fields:
        lines[x] = lines[x] + ['']

# join and write the file
lines = [','.join(x) for x in lines]
lines = '\n'.join(lines)

with open('AwardsPlayers.csv', 'w') as fh:
    fh.write(lines)
```

Now the SQL import will work correctly.

```sql
CREATE TABLE players_awards (
    playerID    varchar,
    award       varchar,
    year        numeric,
    lgID        varchar,
    note        varchar,
    pos         varchar);

COPY players_awards
FROM '/home/ubuntu/professional_hockey/AwardsPlayers.csv'
DELIMITER ','
CSV HEADER;

```

## Coaches

Coaching statistics

```sql
CREATE TABLE coaches (
    coachID    varchar,
    year       numeric,
    tmID       varchar,
    lgID       varchar,
    stint      numeric,
    notes      varchar,
    g          numeric,
    w          numeric,
    l          numeric,
    t          numeric,
    postg      numeric,
    postw      numeric,
    postl      numeric,
    postt      numeric);

COPY coaches
FROM '/home/ubuntu/professional_hockey/Coaches.csv'
DELIMITER ','
CSV HEADER;

```

## Combined shutouts

List of combined shutouts.

```sql
CREATE TABLE combined_shutouts (
    year         numeric,
    month        numeric,
    date_        numeric,
    tmID         varchar,
    oppID        varchar,
    R_P          varchar,
    IDgoalie1    varchar,
    IDgoalie2    varchar);

COPY combined_shutouts
FROM '/home/ubuntu/professional_hockey/CombinedShutouts.csv'
DELIMITER ','
CSV HEADER;

```

## Goalies

Goaltending statistics

A number of the lines have an extra comma at the end. So the these need to be stripped out.

```python
import shutil

with open('Goalies.csv', 'r') as fh:
    lines = fh.readlines()

shutil.copy('Goalies.csv', 'Goalies.bkup')

# split the lines and remove the extras
lines = [x.strip().split(',') for x in lines]
num_fields = min([len(x) for x in lines])
lines = [x[:num_fields] for x in lines]

# join and write the file
lines = [','.join(x) for x in lines]
lines = '\n'.join(lines)

with open('Goalies.csv', 'w') as fh:
    fh.write(lines)
```

Now the SQL import will work.

```sql
CREATE TABLE goalies (
    playerID    varchar,
    year        numeric,
    stint       numeric,
    tmID        varchar,
    lgID        varchar,
    GP          numeric,
    Min         numeric,
    W           numeric,
    L           numeric,
    T_OL        numeric,
    ENG         numeric,
    SHO         numeric,
    GA          numeric,
    SA          numeric,
    PostGP      numeric,
    PostMin     numeric,
    PostW       numeric,
    PostL       numeric,
    PostT       numeric,
    PostENG     numeric,
    PostSHO     numeric,
    PostGA      numeric,
    PostSA      numeric);

COPY goalies
FROM '/home/ubuntu/professional_hockey/Goalies.csv'
DELIMITER ','
CSV HEADER;

```

## Goalies SC

Goaltending for Stanley Cup finals, 1917-18 through 1925-26

```sql
CREATE TABLE goalies_sc (
    playerID    varchar,
    year        numeric,
    tmID        varchar,
    lgID        varchar,
    GP          numeric,
    Min         numeric,
    W           numeric,
    L           numeric,
    T           numeric,
    SHO         numeric,
    GA          numeric);

COPY goalies_sc
FROM '/home/ubuntu/professional_hockey/GoaliesSC.csv'
DELIMITER ','
CSV HEADER;

```

## Goalies shootout

Goaltending for Stanley Cup finals, 1917-18 through 1925-26

```sql
CREATE TABLE goalies_shootout (
    playerID    varchar,
    year        numeric,
    stint       numeric,
    tmID        varchar,
    W           numeric,
    L           numeric,
    SA          numeric,
    GA          numeric);

COPY goalies_shootout
FROM '/home/ubuntu/professional_hockey/GoaliesShootout.csv'
DELIMITER ','
CSV HEADER;

```

## HOF

Hall of Fame information

```sql
CREATE TABLE hof (
    year        numeric,
    hofID       varchar,
    name        varchar,
    category    varchar);

COPY hof
FROM '/home/ubuntu/professional_hockey/HOF.csv'
DELIMITER ','
CSV HEADER;
```

## Master

Names and biographical information

```sql
CREATE TABLE master (
    playerID        varchar,
    coachID         varchar,
    hofID           varchar,
    firstName       varchar,
    lastName        varchar,
    nameNote        varchar,
    nameGiven       varchar,
    nameNick        varchar,
    height          numeric,
    weight          numeric,
    shootCatch      varchar,
    legendsID       varchar,
    ihdbID          numeric,
    hrefID          varchar,
    firstNHL        numeric,
    lastNHL         numeric,
    firstWHA        numeric,
    lastWHA         numeric,
    pos             varchar,
    birthYear       numeric,
    birthMon        numeric,
    birthDay        numeric,
    birthCountry    varchar,
    birthState      varchar,
    birthCity       varchar,
    deathYear       numeric,
    deathMon        numeric,
    deathDay        numeric,
    deathCountry    varchar,
    deathState      varchar,
    deathCity       varchar);

COPY master
FROM '/home/ubuntu/professional_hockey/Master.csv'
DELIMITER ','
CSV HEADER;

```

## Scoring

Scoring statistics

```sql
CREATE TABLE scoring (
    playerID    varchar,
    year        numeric,
    stint       numeric,
    tmID        varchar,
    lgID        varchar,
    pos         varchar,
    GP          numeric,
    G           numeric,
    A           numeric,
    Pts         numeric,
    PIM         numeric,
    P_M         numeric,
    PPG         numeric,
    PPA         numeric,
    SHG         numeric,
    SHA         numeric,
    GWG         numeric,
    GTG         numeric,
    SOG         numeric,
    PostGP      numeric,
    PostG       numeric,
    PostA       numeric,
    PostPts     numeric,
    PostPIM     numeric,
    PostP_M     numeric,
    PostPPG     numeric,
    PostPPA     numeric,
    PostSHG     numeric,
    PostSHA     numeric,
    PostGWG     numeric,
    PostSOG     numeric);

COPY scoring
FROM '/home/ubuntu/professional_hockey/Scoring.csv'
DELIMITER ','
CSV HEADER;

```

## Scoring SC

Scoring for Stanley Cup finals, 1917-18 through 1925-26

```sql
CREATE TABLE scoring_sc (
    playerID    varchar,
    year        numeric,
    tmID        varchar,
    lgID        varchar,
    pos         varchar,
    GP          numeric,
    G           numeric,
    A           numeric,
    Pts         numeric,
    PIM         numeric);

COPY scoring_sc
FROM '/home/ubuntu/professional_hockey/ScoringSC.csv'
DELIMITER ','
CSV HEADER;

```

## Scoring shootout

Scoring statistics for shootouts

```sql
CREATE TABLE scoring_shootout (
    playerID    varchar,
    year        numeric,
    stint       numeric,
    tmID        varchar,
    S           numeric,
    G           numeric,
    GDG         numeric);

COPY scoring_shootout
FROM '/home/ubuntu/professional_hockey/ScoringShootout.csv'
DELIMITER ','
CSV HEADER;

```

## Post season series

Postseason series

```sql
CREATE TABLE series_post (
    year           numeric,
    round          varchar,
    series         varchar,
    tmIDWinner     varchar,
    lgIDWinner     varchar,
    tmIDLoser      varchar,
    lgIDLoser      varchar,
    W              numeric,
    L              numeric,
    T              numeric,
    GoalsWinner    numeric,
    GoalsLoser     numeric,
    note           varchar);

COPY series_post
FROM '/home/ubuntu/professional_hockey/SeriesPost.csv'
DELIMITER ','
CSV HEADER;

```

## Teams

Team regular season statistics

```sql
CREATE TABLE teams (
    year          numeric,
    lgID          varchar,
    tmID          varchar,
    franchID      varchar,
    confID        varchar,
    divID         varchar,
    rank          numeric,
    playoff       varchar,
    G             numeric,
    W             numeric,
    L             numeric,
    T             numeric,
    OTL           numeric,
    Pts           numeric,
    SoW           numeric,
    SoL           numeric,
    GF            numeric,
    GA            numeric,
    name          varchar,
    PIM           numeric,
    BenchMinor    numeric,
    PPG           numeric,
    PPC           numeric,
    SHA           numeric,
    PKG           numeric,
    PKC           numeric,
    SHF           numeric);

COPY teams
FROM '/home/ubuntu/professional_hockey/Teams.csv'
DELIMITER ','
CSV HEADER;

```

## Teams half

First half / second half standings, 1917-18 through 1920-21

```sql
CREATE TABLE teams_half (
    year    numeric,
    lgID    varchar,
    tmID    varchar,
    half    numeric,
    rank    numeric,
    G       numeric,
    W       numeric,
    L       numeric,
    T       numeric,
    GF      numeric,
    GA      numeric);

COPY teams_half
FROM '/home/ubuntu/professional_hockey/TeamsHalf.csv'
DELIMITER ','
CSV HEADER;

```

## Teams splits

First half / second half standings, 1917-18 through 1920-21

```sql
CREATE TABLE team_splits (
    year     numeric,
    lgID     varchar,
    tmID     varchar,
    hW       numeric,
    hL       numeric,
    hT       numeric,
    hOTL     numeric,
    rW       numeric,
    rL       numeric,
    rT       numeric,
    rOTL     numeric,
    SepW     numeric,
    SepL     numeric,
    SepT     numeric,
    SepOL    numeric,
    OctW     numeric,
    OctL     numeric,
    OctT     numeric,
    OctOL    numeric,
    NovW     numeric,
    NovL     numeric,
    NovT     numeric,
    NovOL    numeric,
    DecW     numeric,
    DecL     numeric,
    DecT     numeric,
    DecOL    numeric,
    JanW     numeric,
    JanL     numeric,
    JanT     numeric,
    JanOL    numeric,
    FebW     numeric,
    FebL     numeric,
    FebT     numeric,
    FebOL    numeric,
    MarW     numeric,
    MarL     numeric,
    MarT     numeric,
    MarOL    numeric,
    AprW     numeric,
    AprL     numeric,
    AprT     numeric,
    AprOL    numeric);

COPY team_splits
FROM '/home/ubuntu/professional_hockey/TeamSplits.csv'
DELIMITER ','
CSV HEADER;

```

## Teams post season

Team postseason statistics

```sql
CREATE TABLE teams_post (
    year          numeric,
    lgID          varchar,
    tmID          varchar,
    G             numeric,
    W             numeric,
    L             numeric,
    T             numeric,
    GF            numeric,
    GA            numeric,
    PIM           numeric,
    BenchMinor    numeric,
    PPG           numeric,
    PPC           numeric,
    SHA           numeric,
    PKG           numeric,
    PKC           numeric,
    SHF           numeric);

COPY teams_post
FROM '/home/ubuntu/professional_hockey/TeamsPost.csv'
DELIMITER ','
CSV HEADER;

```

## Teams SC

Team Stanley Cup finals statistics, 1917-18 through 1925-26

```sql
CREATE TABLE teams_sc (
    year    numeric,
    lgID    varchar,
    tmID    varchar,
    G       numeric,
    W       numeric,
    L       numeric,
    T       numeric,
    GF      numeric,
    GA      numeric,
    PIM     numeric);

COPY teams_sc
FROM '/home/ubuntu/professional_hockey/TeamsSC.csv'
DELIMITER ','
CSV HEADER;

```

## Team vs team

Team vs. team results

```sql
CREATE TABLE team_vs_team (
    year     numeric,
    lgID     varchar,
    tmID     varchar,
    oppID    varchar,
    W        numeric,
    L        numeric,
    T        numeric,
    OTL      numeric);

COPY team_vs_team
FROM '/home/ubuntu/professional_hockey/TeamVsTeam.csv'
DELIMITER ','
CSV HEADER;

```