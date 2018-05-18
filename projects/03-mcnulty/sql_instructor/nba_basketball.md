# NBA Basketball

Notes, tips, and SQL commands for importing the NBA basketball data set into PostgreSQL.

## Basketball abbreviations

A key to the abbreviations used in other tables

```sql
CREATE TABLE basketball_abbrev (
    abbrev_type    varchar,
    code           varchar,
    full_name      varchar);

COPY basketball_abbrev
FROM '/home/ubuntu/professional_basketball/basketball_abbrev.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball coaches awards

Coaching awards, per year

```sql
CREATE TABLE basketball_coaches_awards (
    year       numeric,
    coachID    varchar,
    award      varchar,
    lgID       varchar,
    note       varchar);

COPY basketball_coaches_awards
FROM '/home/ubuntu/professional_basketball/basketball_awards_coaches.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball players awards

Player awards, per year

```sql
CREATE TABLE basketball_players_awards (
    playerID    varchar,
    award       varchar,
    year        numeric,
    lgID        varchar,
    note        varchar,
    pos         varchar);

COPY basketball_players_awards
FROM '/home/ubuntu/professional_basketball/basketball_awards_players.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball coaches

Stats for each coach, per year

```sql
CREATE TABLE basketball_coaches (
    coachID        varchar,
    year           numeric,
    tmID           varchar,
    lgID           varchar,
    stint          numeric,
    won            numeric,
    lost           numeric,
    post_wins      numeric,
    post_losses    numeric);

COPY basketball_coaches
FROM '/home/ubuntu/professional_basketball/basketball_coaches.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball draft

Draft information, per year

```sql
CREATE TABLE basketball_draft (
    draftYear         numeric,
    draftRound        numeric,
    draftSelection    numeric,
    draftOverall      numeric,
    tmID              varchar,
    firstName         varchar,
    lastName          varchar,
    suffixName        varchar,
    playerID          varchar,
    draftFrom         varchar,
    lgID              varchar);

COPY basketball_draft
FROM '/home/ubuntu/professional_basketball/basketball_draft.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball HOF

Hall of Fame information, per year

```sql
CREATE TABLE basketball_hof (
    year        numeric,
    hofID       varchar,
    name        varchar,
    category    varchar);

COPY basketball_hof
FROM '/home/ubuntu/professional_basketball/basketball_hof.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball master

Biographical information for all the players and coaches

Note that the date formats in `birthDate` and `deathDate` are not accepted by SQL as a valid timestamp, so students will have to do some manipulation prior or after import to fix if desired.

```sql
CREATE TABLE basketball_master (
    bioID            varchar,
    useFirst         varchar,
    firstName        varchar,
    middleName       varchar,
    lastName         varchar,
    nameGiven        varchar,
    fullGivenName    varchar,
    nameSuffix       varchar,
    nameNick         varchar,
    pos              varchar,
    firstseason      numeric,
    lastseason       numeric,
    height           numeric,
    weight           numeric,
    college          varchar,
    collegeOther     varchar,
    birthDate        varchar,
    birthCity        varchar,
    birthState       varchar,
    birthCountry     varchar,
    highSchool       varchar,
    hsCity           varchar,
    hsState          varchar,
    hsCountry        varchar,
    deathDate        varchar,
    race             varchar);

COPY basketball_master
FROM '/home/ubuntu/professional_basketball/basketball_master.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball all-stars

Individual player stats for the All-Star Game, per year


```sql
CREATE TABLE basketball_allstar (
    player_id          varchar,
    last_name          varchar,
    first_name         varchar,
    season_id          numeric,
    conference         varchar,
    league_id          varchar,
    games_played       numeric,
    minutes            numeric,
    points             numeric,
    o_rebounds         numeric,
    d_rebounds         numeric,
    rebounds           numeric,
    assists            numeric,
    steals             numeric,
    blocks             numeric,
    turnovers          numeric,
    personal_fouls     numeric,
    fg_attempted       numeric,
    fg_made            numeric,
    ft_attempted       numeric,
    ft_made            numeric,
    three_attempted    numeric,
    three_made         numeric);

COPY basketball_allstar
FROM '/home/ubuntu/professional_basketball/basketball_player_allstar.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball players

Stats for each player, per year

```sql
CREATE TABLE basketball_players (
    playerID              varchar,
    year                  numeric,
    stint                 numeric,
    tmID                  varchar,
    lgID                  varchar,
    GP                    numeric,
    GS                    numeric,
    minutes               numeric,
    points                numeric,
    oRebounds             numeric,
    dRebounds             numeric,
    rebounds              numeric,
    assists               numeric,
    steals                numeric,
    blocks                numeric,
    turnovers             numeric,
    PF                    numeric,
    fgAttempted           numeric,
    fgMade                numeric,
    ftAttempted           numeric,
    ftMade                numeric,
    threeAttempted        numeric,
    threeMade             numeric,
    PostGP                numeric,
    PostGS                numeric,
    PostMinutes           numeric,
    PostPoints            numeric,
    PostoRebounds         numeric,
    PostdRebounds         numeric,
    PostRebounds          numeric,
    PostAssists           numeric,
    PostSteals            numeric,
    PostBlocks            numeric,
    PostTurnovers         numeric,
    PostPF                numeric,
    PostfgAttempted       numeric,
    PostfgMade            numeric,
    PostftAttempted       numeric,
    PostftMade            numeric,
    PostthreeAttempted    numeric,
    PostthreeMade         numeric,
    note                  varchar);

COPY basketball_players
FROM '/home/ubuntu/professional_basketball/basketball_players.csv'
DELIMITER ','
CSV HEADER;

```

## Basketbal series

Information on post-season winners, per year

```sql
CREATE TABLE basketball_series_post_season (
    year          numeric,
    round         varchar,
    series        varchar,
    tmIDWinner    varchar,
    lgIDWinner    varchar,
    tmIDLoser     varchar,
    lgIDLoser     varchar,
    W             numeric,
    L             numeric);

COPY basketball_series_post_season
FROM '/home/ubuntu/professional_basketball/basketball_series_post.csv'
DELIMITER ','
CSV HEADER;

```

## Basketball teams

Stats on each team, per year


```sql
CREATE TABLE basketball_teams (
    year           numeric,
    lgID           varchar,
    tmID           varchar,
    franchID       varchar,
    confID         varchar,
    divID          varchar,
    rank           numeric,
    confRank       numeric,
    playoff        varchar,
    name           varchar,
    o_fgm          numeric,
    o_fga          numeric,
    o_ftm          numeric,
    o_fta          numeric,
    o_3pm          numeric,
    o_3pa          numeric,
    o_oreb         numeric,
    o_dreb         numeric,
    o_reb          numeric,
    o_asts         numeric,
    o_pf           numeric,
    o_stl          numeric,
    o_to           numeric,
    o_blk          numeric,
    o_pts          numeric,
    d_fgm          numeric,
    d_fga          numeric,
    d_ftm          numeric,
    d_fta          numeric,
    d_3pm          numeric,
    d_3pa          numeric,
    d_oreb         numeric,
    d_dreb         numeric,
    d_reb          numeric,
    d_asts         numeric,
    d_pf           numeric,
    d_stl          numeric,
    d_to           numeric,
    d_blk          numeric,
    d_pts          numeric,
    o_tmRebound    numeric,
    d_tmRebound    numeric,
    homeWon        numeric,
    homeLost       numeric,
    awayWon        numeric,
    awayLost       numeric,
    neutWon        numeric,
    neutLoss       numeric,
    confWon        numeric,
    confLoss       numeric,
    divWon         numeric,
    divLoss        numeric,
    pace           numeric,
    won            numeric,
    lost           numeric,
    games          numeric,
    min            numeric,
    arena          varchar,
    attendance     numeric,
    bbtmID         varchar);

COPY basketball_teams
FROM '/home/ubuntu/professional_basketball/basketball_teams.csv'
DELIMITER ','
CSV HEADER;

```