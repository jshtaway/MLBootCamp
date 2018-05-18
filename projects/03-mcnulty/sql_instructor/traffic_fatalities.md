# Traffic Fatalities

Files released by the (NHTSA) National Highway Traffic Safety Administration.

Documentation for this database is available online via the [FARS Manual](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812315).

## Accident

The Accident data file includes crash data.

```sql
CREATE TABLE accident (
    STATE         numeric,
    ST_CASE       numeric,
    VE_TOTAL      numeric,
    VE_FORMS      numeric,
    PVH_INVL      numeric,
    PEDS          numeric,
    PERNOTMVIT    numeric,
    PERMVIT       numeric,
    PERSONS       numeric,
    COUNTY        numeric,
    CITY          numeric,
    DAY           numeric,
    MONTH         numeric,
    YEAR          numeric,
    DAY_WEEK      numeric,
    HOUR          numeric,
    MINUTE        numeric,
    NHS           numeric,
    RUR_URB       numeric,
    FUNC_SYS      numeric,
    RD_OWNER      numeric,
    ROUTE         numeric,
    TWAY_ID       varchar,
    TWAY_ID2      varchar,
    MILEPT        numeric,
    LATITUDE      numeric,
    LONGITUD      numeric,
    SP_JUR        numeric,
    HARM_EV       numeric,
    MAN_COLL      numeric,
    RELJCT1       numeric,
    RELJCT2       numeric,
    TYP_INT       numeric,
    WRK_ZONE      numeric,
    REL_ROAD      numeric,
    LGT_COND      numeric,
    WEATHER1      numeric,
    WEATHER2      numeric,
    WEATHER       numeric,
    SCH_BUS       numeric,
    RAIL          varchar,
    NOT_HOUR      numeric,
    NOT_MIN       numeric,
    ARR_HOUR      numeric,
    ARR_MIN       numeric,
    HOSP_HR       numeric,
    HOSP_MN       numeric,
    CF1           numeric,
    CF2           numeric,
    CF3           numeric,
    FATALS        numeric,
    DRUNK_DR      numeric);

COPY accident
FROM '/home/ubuntu/traffic_fatalities/accident.csv'
DELIMITER ','
CSV HEADER;
```

## Crash event

The Cevent data file includes harmful and non-harmful events in the crash.

```sql
CREATE TABLE cevent (
    STATE       numeric,
    ST_CASE     numeric,
    EVENTNUM    numeric,
    VNUMBER1    numeric,
    AOI1        numeric,
    SOE         numeric,
    VNUMBER2    numeric,
    AOI2        numeric);

COPY cevent
FROM '/home/ubuntu/traffic_fatalities/cevent.csv'
DELIMITER ','
CSV HEADER;
```

## Damage

The Damage data file identifies each area of damage (as a separate record). 

```sql
CREATE TABLE damage (
    STATE      numeric,
    ST_CASE    numeric,
    VEH_NO     numeric,
    MDAREAS    numeric);

COPY damage
FROM '/home/ubuntu/traffic_fatalities/damage.csv'
DELIMITER ','
CSV HEADER;
```

## Driver distraction

The Distract data file identifies each driver distraction (as a separate record).

```sql
CREATE TABLE distract (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    MDRDSTRD    numeric);

COPY distract
FROM '/home/ubuntu/traffic_fatalities/distract.csv'
DELIMITER ','
CSV HEADER;
```

## Driver impairment

The Drimpair data file identifies each driver impairment (as a separate record).

```sql
CREATE TABLE drimpair (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    DRIMPAIR    numeric);

COPY drimpair
FROM '/home/ubuntu/traffic_fatalities/drimpair.csv'
DELIMITER ','
CSV HEADER;
```

## Factor

The Factor data file identifies each vehicle factor.

```sql
CREATE TABLE factor (
    STATE      numeric,
    ST_CASE    numeric,
    VEH_NO     numeric,
    MFACTOR    numeric);

COPY factor
FROM '/home/ubuntu/traffic_fatalities/factor.csv'
DELIMITER ','
CSV HEADER;
```

## Maneuver (avoidance attempts)

The Maneuver data file identifies each avoidance attempt

```sql
CREATE TABLE maneuver (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    MDRMANAV    numeric);

COPY maneuver
FROM '/home/ubuntu/traffic_fatalities/maneuver.csv'
DELIMITER ','
CSV HEADER;
```

## Motorist impariment

The Mimpair data file identifies each motorist impairment.

```sql
CREATE TABLE miper (
    ST_CASE    numeric,
    VEH_NO     numeric,
    PER_NO     numeric,
    P1         numeric,
    P2         numeric,
    P3         numeric,
    P4         numeric,
    P5         numeric,
    P6         numeric,
    P7         numeric,
    P8         numeric,
    P9         numeric,
    P10        numeric);

COPY miper
FROM '/home/ubuntu/traffic_fatalities/miper.csv'
DELIMITER ','
CSV HEADER;
```

## Non-motorist impairment

The Nmimpair data file identifies each non-motorist impairment

```sql
CREATE TABLE nmimpair (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    PER_NO      numeric,
    NMIMPAIR    numeric);

COPY nmimpair
FROM '/home/ubuntu/traffic_fatalities/nmimpair.csv'
DELIMITER ','
CSV HEADER;
```

## Non-motorist prior

The Nmprior data file identifies each non-motorist action at the time of their involvement in the crash 

```sql
CREATE TABLE nmprior (
    STATE      numeric,
    ST_CASE    numeric,
    VEH_NO     numeric,
    PER_NO     numeric,
    MPR_ACT    numeric);

COPY nmprior
FROM '/home/ubuntu/traffic_fatalities/nmprior.csv'
DELIMITER ','
CSV HEADER;
```

## Park work

The Parkwork data file includes Vehicle data elements applicable to Parked and Working Vehicles.

```sql
CREATE TABLE parkwork (
    STATE        numeric,
    ST_CASE      numeric,
    VEH_NO       numeric,
    PVE_FORMS    numeric,
    PNUMOCCS     numeric,
    PDAY         numeric,
    PMONTH       numeric,
    PHOUR        numeric,
    PMINUTE      numeric,
    PHARM_EV     numeric,
    PMAN_COLL    numeric,
    PTYPE        numeric,
    PHIT_RUN     numeric,
    PREG_STAT    numeric,
    POWNER       numeric,
    PMAKE        numeric,
    PMODEL       numeric,
    PMAK_MOD     numeric,
    PBODYTYP     numeric,
    PMODYEAR     numeric,
    PVIN         varchar,
    PVIN_1       varchar,
    PVIN_2       varchar,
    PVIN_3       varchar,
    PVIN_4       varchar,
    PVIN_5       varchar,
    PVIN_6       varchar,
    PVIN_7       varchar,
    PVIN_8       varchar,
    PVIN_9       varchar,
    PVIN_10      varchar,
    PVIN_11      varchar,
    PVIN_12      varchar,
    PTRAILER     numeric,
    PMCARR_I1    numeric,
    PMCARR_I2    varchar,
    PMCARR_ID    varchar,
    PGVWR        numeric,
    PV_CONFIG    numeric,
    PCARGTYP     numeric,
    PHAZ_INV     numeric,
    PHAZPLAC     numeric,
    PHAZ_ID      numeric,
    PHAZ_CNO     numeric,
    PHAZ_REL     numeric,
    PBUS_USE     numeric,
    PSP_USE      numeric,
    PEM_USE      numeric,
    PUNDERIDE    numeric,
    PIMPACT1     numeric,
    PVEH_SEV     numeric,
    PTOWED       numeric,
    PM_HARM      numeric,
    PVEH_SC1     numeric,
    PVEH_SC2     numeric,
    PFIRE        numeric,
    PDEATHS      numeric);

COPY parkwork
FROM '/home/ubuntu/traffic_fatalities/parkwork.csv'
DELIMITER ','
CSV HEADER;
```

## Pedestrian, bicyclist, and personal conveyance data

The Pbtype data file includes data on pedestrians, bicyclists, and people on personal conveyances.

```sql
CREATE TABLE pbtype (
    STATE        numeric,
    ST_CASE      numeric,
    VEH_NO       numeric,
    PER_NO       numeric,
    PBPTYPE      numeric,
    PBAGE        numeric,
    PBSEX        numeric,
    PBCWALK      numeric,
    PBSWALK      numeric,
    PBSZONE      numeric,
    PEDCTYPE     numeric,
    BIKECTYPE    numeric,
    PEDLOC       numeric,
    BIKELOC      numeric,
    PEDPOS       numeric,
    BIKEPOS      numeric,
    PEDDIR       numeric,
    BIKEDIR      numeric,
    MOTDIR       numeric,
    MOTMAN       numeric,
    PEDLEG       numeric,
    PEDSNR       varchar,
    PEDCGP       numeric,
    BIKECGP      numeric);

COPY pbtype
FROM '/home/ubuntu/traffic_fatalities/pbtype.csv'
DELIMITER ','
CSV HEADER;
```

## Person

The Person data file includes motorist and non-motorist data.

```sql
CREATE TABLE person (
    STATE         numeric,
    ST_CASE       numeric,
    VE_FORMS      numeric,
    VEH_NO        numeric,
    PER_NO        numeric,
    STR_VEH       numeric,
    COUNTY        numeric,
    DAY           numeric,
    MONTH         numeric,
    HOUR          numeric,
    MINUTE        numeric,
    RUR_URB       numeric,
    FUNC_SYS      numeric,
    HARM_EV       numeric,
    MAN_COLL      numeric,
    SCH_BUS       numeric,
    MAKE          numeric,
    MAK_MOD       numeric,
    BODY_TYP      numeric,
    MOD_YEAR      numeric,
    TOW_VEH       numeric,
    SPEC_USE      numeric,
    EMER_USE      numeric,
    ROLLOVER      numeric,
    IMPACT1       numeric,
    FIRE_EXP      numeric,
    AGE           numeric,
    SEX           numeric,
    PER_TYP       numeric,
    INJ_SEV       numeric,
    SEAT_POS      numeric,
    REST_USE      numeric,
    REST_MIS      numeric,
    AIR_BAG       numeric,
    EJECTION      numeric,
    EJ_PATH       numeric,
    EXTRICAT      numeric,
    DRINKING      numeric,
    ALC_DET       numeric,
    ALC_STATUS    numeric,
    ATST_TYP      numeric,
    ALC_RES       numeric,
    DRUGS         numeric,
    DRUG_DET      numeric,
    DSTATUS       numeric,
    DRUGTST1      numeric,
    DRUGTST2      numeric,
    DRUGTST3      numeric,
    DRUGRES1      numeric,
    DRUGRES2      numeric,
    DRUGRES3      numeric,
    HOSPITAL      numeric,
    DOA           numeric,
    DEATH_DA      numeric,
    DEATH_MO      numeric,
    DEATH_YR      numeric,
    DEATH_HR      numeric,
    DEATH_MN      numeric,
    DEATH_TM      numeric,
    LAG_HRS       numeric,
    LAG_MINS      numeric,
    P_SF1         numeric,
    P_SF2         numeric,
    P_SF3         numeric,
    WORK_INJ      numeric,
    HISPANIC      numeric,
    RACE          numeric,
    LOCATION      numeric);

COPY person
FROM '/home/ubuntu/traffic_fatalities/person.csv'
DELIMITER ','
CSV HEADER;
```

## Vehicle

The Vehicle data file includes in-transport motor vehicle data as well as driver and precrash data.


```sql
CREATE TABLE vehicle (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    VE_FORMS    numeric,
    NUMOCCS     numeric,
    DAY         numeric,
    MONTH       numeric,
    HOUR        numeric,
    MINUTE      numeric,
    HARM_EV     numeric,
    MAN_COLL    numeric,
    UNITTYPE    numeric,
    HIT_RUN     numeric,
    REG_STAT    numeric,
    OWNER       numeric,
    MAKE        numeric,
    MODEL       numeric,
    MAK_MOD     numeric,
    BODY_TYP    numeric,
    MOD_YEAR    numeric,
    VIN         varchar,
    VIN_1       varchar,
    VIN_2       varchar,
    VIN_3       varchar,
    VIN_4       varchar,
    VIN_5       varchar,
    VIN_6       varchar,
    VIN_7       varchar,
    VIN_8       varchar,
    VIN_9       varchar,
    VIN_10      varchar,
    VIN_11      varchar,
    VIN_12      varchar,
    TOW_VEH     numeric,
    J_KNIFE     numeric,
    MCARR_I1    numeric,
    MCARR_I2    varchar,
    MCARR_ID    varchar,
    GVWR        numeric,
    V_CONFIG    numeric,
    CARGO_BT    numeric,
    HAZ_INV     numeric,
    HAZ_PLAC    numeric,
    HAZ_ID      numeric,
    HAZ_CNO     numeric,
    HAZ_REL     numeric,
    BUS_USE     numeric,
    SPEC_USE    numeric,
    EMER_USE    numeric,
    TRAV_SP     numeric,
    UNDERIDE    numeric,
    ROLLOVER    numeric,
    ROLINLOC    numeric,
    IMPACT1     numeric,
    DEFORMED    numeric,
    TOWED       numeric,
    M_HARM      numeric,
    VEH_SC1     numeric,
    VEH_SC2     numeric,
    FIRE_EXP    numeric,
    DR_PRES     numeric,
    L_STATE     numeric,
    DR_ZIP      numeric,
    L_STATUS    numeric,
    L_TYPE      numeric,
    CDL_STAT    numeric,
    L_ENDORS    numeric,
    L_COMPL     numeric,
    L_RESTRI    numeric,
    DR_HGT      numeric,
    DR_WGT      numeric,
    PREV_ACC    numeric,
    PREV_SUS    numeric,
    PREV_DWI    numeric,
    PREV_SPD    numeric,
    PREV_OTH    numeric,
    FIRST_MO    numeric,
    FIRST_YR    numeric,
    LAST_MO     numeric,
    LAST_YR     numeric,
    SPEEDREL    numeric,
    DR_SF1      numeric,
    DR_SF2      numeric,
    DR_SF3      numeric,
    DR_SF4      numeric,
    VTRAFWAY    numeric,
    VNUM_LAN    numeric,
    VSPD_LIM    numeric,
    VALIGN      numeric,
    VPROFILE    numeric,
    VPAVETYP    numeric,
    VSURCOND    numeric,
    VTRAFCON    numeric,
    VTCONT_F    numeric,
    P_CRASH1    numeric,
    P_CRASH2    numeric,
    P_CRASH3    numeric,
    PCRASH4     numeric,
    PCRASH5     numeric,
    ACC_TYPE    numeric,
    DEATHS      numeric,
    DR_DRINK    numeric);

COPY vehicle
FROM '/home/ubuntu/traffic_fatalities/vehicle.csv'
DELIMITER ','
CSV HEADER;
```

## Vehicle event

The Vevent data file includes harmful and non-harmful events for each in-transport motor vehicle.

```sql
CREATE TABLE vevent (
    STATE        numeric,
    ST_CASE      numeric,
    EVENTNUM     numeric,
    VEH_NO       numeric,
    VEVENTNUM    numeric,
    VNUMBER1     numeric,
    AOI1         numeric,
    SOE          numeric,
    VNUMBER2     numeric,
    AOI2         numeric);

COPY vevent
FROM '/home/ubuntu/traffic_fatalities/vevent.csv'
DELIMITER ','
CSV HEADER;
```

## VIN decode

The Vindecode data file provides vehicle specification data for all vehicle types, mainly passenger vehicles, trucks and motorcycles.

There are some nan entries which must be removed for numeric columns to be used.

```bash
sed -i.bak 's/NA//g' vindecode.csv
```

```sql
CREATE TABLE vindecode (
    STATE         numeric,
    ST_CASE       numeric,
    VEH_NO        numeric,
    NCICMAKE      varchar,
    VINYEAR       numeric,
    VEHTYPE       varchar,
    VEHTYPE_T     varchar,
    VINMAKE_T     varchar,
    VINMODEL_T    varchar,
    VINTRIM_T     varchar,
    VINTRIM1_T    varchar,
    VINTRIM2_T    varchar,
    VINTRIM3_T    varchar,
    VINTRIM4_T    varchar,
    BODYSTYL      varchar,
    BODYSTYL_T    varchar,
    DOORS         numeric,
    WHEELS        numeric,
    DRIVWHLS      numeric,
    MFG           varchar,
    MFG_T         varchar,
    DISPLCI       numeric,
    DISPLCC       numeric,
    CYLNDRS       varchar,
    CYCLES        numeric,
    FUEL          varchar,
    FUEL_T        varchar,
    FUELINJ       varchar,
    FUELINJ_T     varchar,
    CARBTYPE      varchar,
    CARBTYPE_T    varchar,
    CARBBRLS      numeric,
    GVWRANGE      numeric,
    GVWRANGE_T    varchar,
    WHLBSH        numeric,
    WHLBLG        numeric,
    TIREDESC_F    numeric,
    PSI_F         numeric,
    TIRESZ_F      varchar,
    TIRESZ_F_T    varchar,
    TIREDESC_R    numeric,
    PSI_R         numeric,
    REARSIZE      numeric,
    REARSIZE_T    varchar,
    TONRATING     varchar,
    SHIPWEIGHT    numeric,
    MSRP          numeric,
    DRIVETYP      varchar,
    DRIVETYP_T    varchar,
    SALECTRY      varchar,
    SALECTRY_T    varchar,
    ABS           varchar,
    ABS_T         varchar,
    SECURITY      varchar,
    SECURITY_T    varchar,
    DRL           varchar,
    DRL_T         varchar,
    RSTRNT        varchar,
    RSTRNT_T      varchar,
    TKCAB         varchar,
    TKCAB_T       varchar,
    TKAXLEF       varchar,
    TKAXLEF_T     varchar,
    TKAXLER       varchar,
    TKAXLER_T     varchar,
    TKBRAK        varchar,
    TKBRAK_T      varchar,
    ENGMFG        varchar,
    ENGMFG_T      varchar,
    ENGMODEL      varchar,
    TKDUTY        varchar,
    TKDUTY_T      varchar,
    TKBEDL        varchar,
    TKBEDL_T      varchar,
    SEGMNT        varchar,
    SEGMNT_T      varchar,
    PLANT         varchar,
    PLNTCTRY_T    varchar,
    PLNTCITY      varchar,
    PLNTCTRY      varchar,
    PLNTSTAT      varchar,
    PLNTSTAT_T    varchar,
    ORIGIN        varchar,
    ORIGIN_T      varchar,
    DISPCLMT      numeric,
    BLOCKTYPE     varchar,
    ENGHEAD       varchar,
    ENGHEAD_T     varchar,
    VLVCLNDR      numeric,
    VLVTOTAL      numeric,
    ENGVINCD      varchar,
    INCOMPLT      varchar,
    BATTYP        varchar,
    BATTYP_T      varchar,
    BATKWRTG      varchar,
    BATVOLT       numeric,
    SUPCHRGR      varchar,
    SUPCHRGR_T    varchar,
    TURBO         varchar,
    TURBO_T       varchar,
    ENGVVT        varchar,
    MCYUSAGE      varchar,
    MCYUSAGE_T    varchar);

COPY vindecode
FROM '/home/ubuntu/traffic_fatalities/vindecode.csv'
DELIMITER ','
CSV HEADER;
```

## Visual obstruction

The Vision data file identifies each visual obstruction.

```sql
CREATE TABLE vision (
    STATE       numeric,
    ST_CASE     numeric,
    VEH_NO      numeric,
    MVISOBSC    numeric);

COPY vision
FROM '/home/ubuntu/traffic_fatalities/vision.csv'
DELIMITER ','
CSV HEADER;
```