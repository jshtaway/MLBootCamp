## PostgreSQL setup and loading data


### Install PostgreSQL

(Mostly following the [Ubuntu directions](https://help.ubuntu.com/community/PostgreSQL).)

```bash
sudo apt-get install postgresql postgresql-contrib
```

This will install _and start up_ Postgres. You can check:

```bash
ps awx | grep post
```

On Ubuntu, servers are started and stopped mostly with [upstart](http://upstart.ubuntu.com/). Try:

```bash
sudo service postgresql status
sudo service postgresql stop
sudo service postgresql start
```

Installing Postgres also created a `postgres` user on your computer. But we want to be able to log in as ourselves. So:

```bash
sudo -u postgres createuser --superuser my_user_name
sudo -u postgres psql
# now in psql...
\password my_user_name
# exit psql...
sudo -u postgres createdb my_user_name
```

Now you can go to town with just `psql`! Explore a little with `help`, `\?`, `\l`, and `\d`.


### Make a database

Check what databases you have so far with `\l`.

You can create a new database with `CREATE DATABASE database_name;`.

Case doesn't matter, but to make it clear what's a SQL word and what's chosen by us I'll follow the ugly SQL convention of capitalizing like a crazy person.

Let's make a database called `endor`.

```sql
CREATE DATABASE endor;
```

Now connect to it:

```sql
\connect endor;
```

Use `\d` to see that there are not yet any tables (relations) in the database. So let's create one.


### Make a table

We have to specify the schema of our table, with detail about [data types](http://www.postgresql.org/docs/9.3/static/datatype.html). There are a bunch of data types, but a few are used most commonly.

```sql
CREATE TABLE ewoks (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT,
    accuracy DOUBLE PRECISION
);
```

Now you can see that you have a table with `\d`. And you can see what's in it like this:

```sql
SELECT * FROM ewoks;
```


### Manual data loading / removing

You can load data from inside `psql`:

```sql
INSERT INTO ewoks (name, age, accuracy) VALUES ('Wicket', 8, 0.9);
```

Now `SELECT` to see that your data is there.

Run the `INSERT` again to see what happens.

You can also delete:

```sql
DELETE FROM ewoks WHERE id=2;
```

And finally, you can drop a whole table:

```sql
DROP TABLE ewoks;
```


### Loading data from a file

Make the same `ewoks` table again.

Make a file `ewoks.csv`:

```text
ID,name,years,acc
1,Wicket,8,0.9
```

Postgres can handle CSV input. To load it:

```sql
COPY ewoks FROM '/path/to/ewoks.csv' DELIMITER ',' CSV HEADER;
```

Verify success with `SELECT`.

Check out what happens if you try to run that command a second time.
