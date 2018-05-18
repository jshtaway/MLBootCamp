# Militarized Interstate Disputes

This data set records all instances of when one state threatened, displayed, or used force against another. Version 4.1 covers the 1816-2010 period.

Note that this database carries a citation request, so students should cite appropriately in presentations.

Notes, tips, and SQL commands for importing the militarized interstate disputes data set into PostgreSQL.

## Militarized Interstate Dispute (MID) level data

### MIDA_4.01

Data on MIDs from 1816-2010, at the dispute level. Contains one record per militarized dispute.

```sql
CREATE TABLE MIDA (
    DispNum3    numeric,
    DispNum4    numeric,
    StDay       numeric,
    StMon       numeric,
    StYear      numeric,
    EndDay      numeric,
    EndMon      numeric,
    EndYear     numeric,
    Outcome     numeric,
    Settle      numeric,
    Fatality    numeric,
    FatalPre    numeric,
    MaxDur      numeric,
    MinDur      numeric,
    HiAct       numeric,
    HostLev     numeric,
    Recip       numeric,
    NumA        numeric,
    NumB        numeric,
    Link1       varchar,
    Link2       varchar,
    Link3       numeric,
    Ongo2010    numeric,
    Version     numeric);

COPY MIDA
FROM '/home/ubuntu/militarized_interstate_disputes/MIDA_4.01.csv'
DELIMITER ','
CSV HEADER;
```

### MIDB_4.01

Data on MIDs from 1816-2010, at the participant level. Contains one record per militarized dispute participant.

```sql
CREATE TABLE MIDB (
    DispNum3    numeric,
    DispNum4    numeric,
    StAbb       varchar,
    ccode       numeric,
    StDay       numeric,
    StMon       numeric,
    StYear      numeric,
    EndDay      numeric,
    EndMon      numeric,
    EndYear     numeric,
    SideA       numeric,
    RevState    numeric,
    RevType1    numeric,
    RevType2    numeric,
    Fatality    numeric,
    FataPre     numeric,
    HiAct       numeric,
    HostLev     numeric,
    Orig        numeric,
    Version     numeric);

COPY MIDB
FROM '/home/ubuntu/militarized_interstate_disputes/MIDB_4.01.csv'
DELIMITER ','
CSV HEADER;
```

## Incident-level data and documents

### MIDI_4.01

Data on incidents within MIDs from 1993-2010 (along with disputes ongoing as of 12/31/1992), at the incident level. Contains one record per militarized incident.

```sql
CREATE TABLE MIDI (
    DispNum3     numeric,
    IncidNum3    numeric,
    DispNum4     numeric,
    IncidNum4    numeric,
    StDay        numeric,
    StMon        numeric,
    StYear       numeric,
    EndDay       numeric,
    EndMon       numeric,
    EndYear      numeric,
    Duration     numeric,
    TBI          numeric,
    Fatality     numeric,
    FatalPre     numeric,
    Action       numeric,
    HostLev      numeric,
    NumA         numeric,
    RevType1     numeric,
    RevType2     numeric,
    Version      numeric);

COPY MIDI
FROM '/home/ubuntu/militarized_interstate_disputes/MIDI_4.01.csv'
DELIMITER ','
CSV HEADER;
```

### MIDIP_4.01

Data on incidents within MIDs from 1993-2010 (along with disputes ongoing as of 12/31/1992), at the incident-participant level. Contains one record per participant in each incident.

```sql
CREATE TABLE MIDIP (
    DispNum3     numeric,
    IncidNum3    numeric,
    DispNum4     numeric,
    IncidNum4    numeric,
    StAbb        varchar,
    ccode        numeric,
    StDay        numeric,
    StMon        numeric,
    StYear       numeric,
    EndDay       numeric,
    EndMon       numeric,
    EndYear      numeric,
    InSide_A     numeric,
    SideA        numeric,
    Fatality     numeric,
    FatalPre     numeric,
    Action       numeric,
    HostLev      numeric,
    RevType1     numeric,
    RevType2     numeric,
    Version      numeric);

COPY MIDIP
FROM '/home/ubuntu/militarized_interstate_disputes/MIDIP_4.01.csv'
DELIMITER ','
CSV HEADER;
```

## Dyadic MID data 

Note that this data is from a previous version of the database.

### MIDDyadic_3.10

Data on dyadic MIDs from 1993-2001 (along with disputes ongoing as of 12/31/1992), at the dyad level. Contains one record per dyadic MID.

```sql
CREATE TABLE MIDDyadic (
    DispNum     numeric,
    DyMIDNum    numeric,
    CCodeA      numeric,
    CCodeB      numeric,
    StDay       numeric,
    StMon       numeric,
    StYear      numeric,
    EndDay      numeric,
    EndMon      numeric,
    EndYear     numeric,
    HiactA      numeric,
    HiactB      numeric,
    HostlevA    numeric,
    HostlevB    numeric,
    SideAA      numeric,
    SideAB      numeric,
    RevstatA    numeric,
    Revtyp1A    numeric,
    Revtyp2A    numeric,
    RevstatB    numeric,
    Revtyp1B    numeric,
    Revtyp2B    numeric,
    OrigA       numeric,
    OrigB       numeric,
    FatalA      numeric,
    FatalB      numeric,
    FatalPrA    numeric,
    FatalPrB    numeric,
    RoleA       numeric,
    RoleB       numeric,
    Reciproc    numeric,
    SideADyA    numeric,
    SideADyB    numeric,
    Version     numeric);

COPY MIDDyadic
FROM '/home/ubuntu/militarized_interstate_disputes/MIDDyadic_v3.10.csv'
DELIMITER ','
CSV HEADER;
```
