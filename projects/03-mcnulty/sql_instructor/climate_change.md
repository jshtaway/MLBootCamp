# Climate Change

Data from a compilation put together by the Berkeley Earth, which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature Study combines 1.6 billion temperature reports from 16 pre-existing archives. It is nicely packaged and allows for slicing into interesting subsets (for example by country). They publish the source data and the code for the transformations they applied. They also use methods that allow weather observations from shorter time series to be included, meaning fewer observations need to be thrown away.

Notes, tips, and SQL commands for importing the climate change data set into PostgreSQL.

## Global temperatures

```sql
CREATE TABLE global_temperatures (
    dt                                        timestamp without time zone,
    LandAverageTemperature                    numeric,
    LandAverageTemperatureUncertainty         numeric,
    LandMaxTemperature                        numeric,
    LandMaxTemperatureUncertainty             numeric,
    LandMinTemperature                        numeric,
    LandMinTemperatureUncertainty             numeric,
    LandAndOceanAverageTemperature            numeric,
    LandAndOceanAverageTemperatureUncertainty numeric);

COPY global_temperatures
FROM '/home/ubuntu/climate_change/GlobalTemperatures.csv'
DELIMITER ','
CSV HEADER;
```

## Global land temperatures by city

This table is extremely large (8.6 million rows) and will take some time to load

```sql
CREATE TABLE global_by_city (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    City                             varchar,
    Country                          varchar,
    Latitude                         varchar,
    Longitude                        varchar);

COPY global_by_city
FROM '/home/ubuntu/climate_change/GlobalLandTemperaturesByCity.csv'
DELIMITER ','
CSV HEADER;
```

## Global land temperatures by country

```sql
CREATE TABLE global_by_country (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    Country                          varchar);

COPY global_by_country
FROM '/home/ubuntu/climate_change/GlobalLandTemperaturesByCountry.csv'
DELIMITER ','
CSV HEADER;
```

## Global land temperatures by major city

```sql
CREATE TABLE global_by_major_city (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    City                             varchar,
    Country                          varchar,
    Latitude                         varchar,
    Longitude                        varchar);

COPY global_by_major_city
FROM '/home/ubuntu/climate_change/GlobalLandTemperaturesByMajorCity.csv'
DELIMITER ','
CSV HEADER;
```

## Global land temperatures by state

```sql
CREATE TABLE global_by_state (
    dt                               timestamp without time zone,
    AverageTemperature               numeric,
    AverageTemperatureUncertainty    numeric,
    State                            varchar,
    Country                          varchar);

COPY global_by_state
FROM '/home/ubuntu/climate_change/GlobalLandTemperaturesByState.csv'
DELIMITER ','
CSV HEADER;
```

