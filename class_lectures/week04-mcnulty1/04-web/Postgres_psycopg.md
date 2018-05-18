
In this walkthru we will first build some more 
tables in our remote Postgres server.  We will 
then alter some configuration settings so that
we will be able to connect with our remote Postgres server locally (via python & pandas).

First, let's ssh into our cloud.. 

```bash
ssh ubuntu 
# Make sure you are home (/home/username)
pwd

```
Let's get some data to work with via the Lahman baseball data


```bash
wget http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip
sudo apt-get install unzip
mkdir baseballdata
unzip lahman-csv_2014-02-14.zip -d baseballdata
```

```sudo -u postgres psql```

```sql
CREATE TABLE IF NOT EXISTS AllstarFull (
	playerID varchar(20) NOT NULL,
	yearID int NOT NULL,
	gameNum varchar(20) NOT NULL,
	gameID varchar(12) DEFAULT NULL,
	teamID text DEFAULT NULL,
	lgID text DEFAULT NULL,
	GP varchar(20) DEFAULT NULL,
	startingPos varchar(20) DEFAULT NULL,
	PRIMARY KEY (playerID,yearID,gameNum)
);


COPY AllstarFull FROM '/home/username/baseballdata/AllstarFull.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS Salaries (
	yearID int NOT NULL,
	teamID varchar(3) NOT NULL,
	lgID varchar(2) NOT NULL,
	playerID varchar(9) NOT NULL,
	salary double precision DEFAULT NULL,
	PRIMARY KEY (yearID,teamID,lgID,playerID)
);

COPY Salaries FROM '/home/username/baseballdata/Salaries.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS Schools (
	schoolID varchar(15) NOT NULL,
	schoolName varchar(255) DEFAULT NULL,
	schoolCity varchar(55) DEFAULT NULL,
	schoolState varchar(55) DEFAULT NULL,
	schoolNick varchar(55) DEFAULT NULL,
	PRIMARY KEY (schoolID)
);

COPY Schools FROM '/home/username/baseballdata/Schools.csv' DELIMITER ',' CSV HEADER;
```

## Connect to Postgres! 

 We want to connect Postgres with SQL Alchemy and psycopg locally.  But first we'll just have to change a few settings.. 

 # \q to get out of sql database 

```bash
sudo su - postgres
nano /etc/postgresql/9.5/main/postgresql.conf
```

On our postgresql.conf: change your
change listen_addresses='localhost' to listen_addresses='*'   
Hint: make sure the line is no longer commented out   
Hint Hint: while in nano you can use control w for search (just search for 'listen_addresses')    

```bash
nano /etc/postgresql/9.5/main/pg_hba.conf
```

On our pg_hba.conf: let's add:
'host    all      all      65.209.60.146/0     trust'

(Save file and exit)

Restart server

```bash
exit
sudo service postgresql restart
```

Now we have to add a rule to the Security 
Group of your AWS instance: 

 
| Type        | Protocol           | Port Range  | Source |
| ------------- |:-------------:| -----:| -----:|
| Custom TCP rule     | TCP | 5432 |Anywhere |


Now-- we will go to your LOCAL bash & install psycopg


```bash
pip install psycopg2
```
