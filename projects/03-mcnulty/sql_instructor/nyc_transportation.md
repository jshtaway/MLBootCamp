# NYC Transportation Data

Notes, tips, and SQL commands for importing the NYC transportation data set into PostgreSQL.

## NYC Yellow Taxi Data

```sql
CREATE TABLE yellow_taxi (
    VendorID              integer,
    tpep_pickup_datetime  timestamp without time zone,
    tpep_dropoff_datetime timestamp without time zone,
    passenger_count       integer,
    trip_distance         numeric,
    pickup_longitude      numeric,
    pickup_latitude       numeric,
    RatecodeID            integer,
    store_and_fwd_flag    varchar,
    dropoff_longitude     numeric,
    dropoff_latitude      numeric,
    payment_type          integer,
    fare_amount           numeric,
    extra                 numeric,
    mta_tax               numeric,
    tip_amount            numeric,
    tolls_amount          numeric,
    improvement_surcharge numeric,
    total_amount          numeric);

COPY yellow_taxi
FROM '/home/ubuntu/nyc_transport/yellow_tripdata_2016-01.csv'
DELIMITER ','
CSV HEADER;
```

### NYC Green Taxi Data

The Green Taxi data has a few more columns than the Yellow Taxi data, although the formats are quite similar.

The data has a blank line with space characters in it between the column labels and the data. These can be removed with sed.

```bash
sed -i.bak '/^\s*$/d' green_tripdata_2016-01.csv
```

The line endings in some of the Green Taxi data files cause issue when imported into SQL. They can be normalized with sed or (even easier) opened with Sublime Text and then set with `File -> Save With Encoding -> UTF-8`.


```sql
CREATE TABLE green_taxi (
    VendorID              integer,
    lpep_pickup_datetime  timestamp without time zone,
    Lpep_dropoff_datetime timestamp without time zone,
    Store_and_fwd_flag    varchar,
    RateCodeID            integer,
    Pickup_longitude      numeric,
    Pickup_latitude       numeric,
    Dropoff_longitude     numeric,
    Dropoff_latitude      numeric,
    Passenger_count       integer,
    Trip_distance         numeric,
    Fare_amount           numeric,
    Extra                 numeric,
    MTA_tax               numeric,
    Tip_amount            numeric,
    Tolls_amount          numeric,
    Ehail_fee             numeric,
    improvement_surcharge numeric,
    Total_amount          numeric,
    Payment_type          integer,
    Trip_type             integer);

COPY green_taxi
FROM '/home/ubuntu/nyc_transport/green_tripdata_2016-01.csv'
DELIMITER ','
CSV HEADER;
```

## NYC For-Hire Vechicle (FHV) Data

The FHV data is quite limited in the fields provided, compared to the Yellow and Green Taxi data.

```sql
CREATE TABLE fhv_cars (
    Dispatching_base_num varchar,
    Pickup_date          timestamp without time zone,
    locationID           integer;

COPY fhv_cars
FROM '/home/ubuntu/nyc_transport/fhv_tripdata_2016-01.csv'
DELIMITER ','
CSV HEADER;
```

## CitiBike Data

There are two different timestamp formats: one with and one without seconds. Some of the data also have fields enclosed in quotes, while other data tables do not.

The same schema can be used to import the data as long as null fields, which are double quoted in the data where fields are enclosed in quotes, are stripped. This can be done using sed.

```bash
sed -i.bak 's/""//g' 201512-citibike-tripdata.csv
```

Then the scheme can be created and files can be successively added using `COPY`.

```sql
CREATE TABLE citbike (
        tripduration             integer,
        starttime                timestamp without time zone,
        stoptime                 timestamp without time zone,
        start_station_id         integer,
        start_station_name       varchar,
        start_station_latitude   numeric,
        start_station_longitude  numeric,
        end_station_id           integer,
        end_station_name         varchar,
        end_station_latitude     numeric,
        end_station_longitude    numeric,
        bikeid                   integer,
        usertype                 varchar,
        birth_year               integer,
        gender                   integer);

COPY citbike
FROM '/home/ubuntu/nyc_transport/201501-citibike-tripdata.csv'
DELIMITER ','
CSV HEADER;
```

## NYC MTA Turnstile Data

Three of the default column names (`DATE`, `TIME`, and `DESC`) are reserved SQL words, so an underscore was added.

```sql
CREATE TABLE turnstile (
    C_A       varchar,
    UNIT      varchar,
    SCP       varchar,
    STATION   varchar,
    LINENAME  varchar,
    DIVISION  varchar,
    DATE_     date,
    TIME_     time without time zone,
    DESC_     varchar,
    ENTRIES   integer,
    EXITS     integer);

COPY turnstile
FROM '/home/ubuntu/nyc_transport/turnstile_161203.txt'
DELIMITER ','
CSV HEADER;
```

## NOAA Weather Data

The data downloaded from NOAA is fixed width and contains varying number of asterisks when a given field is empty. The format of the timestamp (the `YR--MODAHRMN` column) also isn't recognized by PostgreSQL.

The spaces can first be removed and the file converted to a CSV with sed.

```bash
sed -i.bak 's/^ \{1,\}//g;s/ \{1,\}/,/g;s/\*//g' nyc_central_park_hourly_weather.txt
```

The date format can be fixed either later, once the data are imported into Python, or by reading the file with Python (for example) and re-writing it.

```sql
CREATE TABLE weather (
    USAF              integer,
    WBAN              integer,
    YEAR_MO_DA_HR_MN  varchar,
    DIR               integer,
    SPD               integer,
    GUS               integer,
    CLG               integer,
    SKC               varchar,
    L                 varchar,
    M                 varchar,
    H                 varchar,
    VSB               integer,
    MW1               varchar,
    MW2               varchar,
    MW3               varchar,
    MW4               varchar,
    AW1               varchar,
    AW2               varchar,
    AW3               varchar,
    AW4               varchar,
    W                 varchar,
    TEMP              integer,
    DEWP              integer,
    SLP               numeric,
    ALT               numeric,
    STP               numeric,
    MAX               integer,
    MIN               integer,
    PCP01             numeric,
    PCP06             numeric,
    PCP24             numeric,
    PCPXX             numeric,
    SD                varchar);

COPY weather
FROM '/home/ubuntu/nyc_transport/nyc_central_park_hourly_weather.txt'
DELIMITER ','
CSV HEADER;
```

## Uber Data

The Uber Data was obtained by the New York Times' FiveThirtyEight group via a freedom of information (FOI) request. A data set has been posted on [Kaggle](https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city) and there is a [GitHub repo](https://github.com/fivethirtyeight/uber-tlc-foil-response) that is maintained. Because it comes through a FOI request, it is likely not as up-to-date as municipal data sets.

Much of the Uber data set is parsed from the FHV data. Thus, the column format is relatively similar. There are multiple files with varying formats in this data set, but here is an example.

```sql
CREATE TABLE uber (
    Dispatching_base_num varchar,
    Pickup_date          timestamp without time zone,
    Affiliated_base_num  varchar,
    locationID           integer);

COPY uber
FROM '/home/ubuntu/nyc_transport/uber_data/uber-raw-data-janjune-15.csv'
DELIMITER ','
CSV HEADER;
```