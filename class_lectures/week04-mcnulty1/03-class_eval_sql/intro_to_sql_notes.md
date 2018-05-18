**SQL** stands for **Structured Query Langauge**. And it works with/on **Relational Database Systems**. It is the industry standard. 

It is a way of selecting, filtering, organizing and aggregating data.

The data is typical stored on a file system. Both the files system and SQL can be **distributed** and **parellelized**.

The operations of SQL is not unlike Pandas, and since you are all familiar with that, it's probably easier to go over the **differences with Pandas**:

- SQL doesn't distinguish between a dataframe and series, everything is a table in SQL.
- There is no index in SQL the way Pandas has indexes. There are only columns.
- Merge in Pandas is Join in SQL.
- In Pandas you 'sort' and then 'group by'. In SQL you 'group by' and then 'order by'.
- SQL allows you call one or more columns as 'key'. If you do that, operations on that column (where, group by) will be faster.
- SQL allows you to call a column 'primary key'. If you do that, it will require that every row in the table has a unique value for that column.
- Everything in SQL is case insensitive except for the table names.

Relational Database Systems usually have a **set of tables** to avoid redundancies:

- Think of a company that has 1000 costumers, 500 products and 10,000 purchases. The **customer** table would then have 1000 rows with detals like name, address, etc, along with a *customerID*. The **product** table will have details like category, manufacturer, etc, along with a *productID*. The **purchase** table can then just have *customerID*, *productID*, price and date. This way we can get the information we need by joining (merging) the tables.

- In this situation. The *customerID* on the **customer** table might be a 'primary key' (since each customer must have a unique id). And the *customerID* on **purchase** table might be 'foreign key' pointing to the **customer** table (so that an error is triggered if a customerID doesn't exist in the customer table).

This is the order of operation in SQL:

    JOIN
    WHERE
    GROUP BY
    HAVING
    ORDER BY
    LIMIT

Paranthesis can be used to do things in a different order (for example, if we want to do a group by and then a join).
