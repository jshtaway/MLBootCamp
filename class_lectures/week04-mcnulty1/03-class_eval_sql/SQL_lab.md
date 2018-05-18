# SQL Lab

_Structured Query Language_ (SQL) is a very useful [declarative language](http://en.wikipedia.org/wiki/Declarative_programming) for working with data. It is usually supported (with some variation) by relational databases. The tutorialspoint [SQL Quick Guide](http://www.tutorialspoint.com/sql/sql-quick-guide.htm) is a handy cheat sheet for a lot of the syntax. As a data user, access to data will usually consist of a more or less complicated `SELECT` statement.

For joining data with SQL, this [Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is quite good. One thing to note is that "join" will also often be known as "merge" in statistical software.

This lab uses the SQL playground provided in-browser by [W3Schools](http://www.w3schools.com/). Click [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) to go straight to the playground.

This is a pre-populated data environment with nothing to install and no risk of breaking anything. The data there is from a commonly-used example database ([info](http://northwinddatabase.codeplex.com/)). Nice!


## Guided Examples

**Basic Queries**

1) Retrieve all Customers from Madrid

```sql
SELECT
    * 
FROM
    Customers
WHERE
    City='Madrid';
```

2) How many customers are there in each city?

```sql
SELECT
    City, COUNT(*)
FROM
    Customers
GROUP BY
    City;
```

3) What is the most common city for customers? (Find all city counts and sort in descending order)

```sql
SELECT
    City, COUNT(*) AS count 
FROM
    Customers 
GROUP BY
    City 
ORDER BY
    count DESC;
```

4) What category has the most products?

```sql
SELECT
    CategoryName,
    COUNT(*) AS ProductCount
FROM
    Categories
  JOIN
    Products
  ON
    Categories.CategoryID = Products.CategoryID
GROUP BY
    CategoryName
ORDER BY 
    ProductCount DESC;
```


**Basic Practice**

 * Which customers are from the UK?
 * What is the name of the customer who has the most orders?
 * Which supplier has the highest average product price?
 * How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
 * What category appears in the most orders?
 * What was the total cost for each order?
 * Which employee made the most sales (by total cost)?
 * Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
 * Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
 
 
**More Advanced Queries**

1) What is the average number of products that a supplier sells?

   Multiple aggregation steps, we'll use a **subquery**. A subquery must be a valid query on its own, and can then be treated as a table to query in the normal way. A very common use case is to chain multiple aggregation steps, as required in this problem (count products, then average the counts)  

```sql
SELECT AVG(num_products) FROM 
(
   SELECT SupplierID, COUNT(ProductName) AS num_products FROM Products
   GROUP BY SupplierID
)
```

2) What are all the products sold by the suppliers that sell the 3 most expensive products?

   Another common subquery use - using a subquery to filter a table. In this case we use the subquery to determine which      suppliers sell the 3 most expensive products, and chain this to the `WHERE` condition of the bigger (joined) table.

```sql
SELECT SupplierName, ProductName, Price FROM Suppliers
JOIN Products ON Suppliers.SupplierID = Products.SupplierID
WHERE Suppliers.SupplierID IN
(
   SELECT SupplierID FROM Products
   ORDER BY Price DESC
   LIMIT 3
)
ORDER BY SupplierName
```

3) A subquery and a window function! Imagine you collect data on user logins to an app in the UserLogs table, and are asked: how do you extract a table with records for only 2nd time logins across users? I.e. if user Bob logged in at 9:15, 9:23, 9:55, etc. we want only the 9:23 record.

   `OVER (PARTITION BY...)` is the window definition. It performs a similar role to transform in Pandas. The window definition tells SQL how to run a calculation for each table row over some partition of the table. In the case below, for every row in UserLogs the subquery will return the user-login number for that row. Then we filter on the subquery to get only 2nd user-logins.

```sql
SELECT * FROM
(
   SELECT *,
         ROW_NUMBER() OVER (PARTITION BY UserID ORDER BY LoginTime) AS rn
   FROM UserLogs
)
WHERE rn = 2
```

Warning: the SQL playground will not recognize the window syntax.

**More Advanced Practice**

 * What product has the highest total shipping quantity for the shipper with the most total orders?
 * Figure out how you could use SQL window functions to compute a rolling difference partitioned by group. I.e. use SQL to replicate pandas groupby.diff.transform method we used to get daily entry counts for the MTA turnstiles. HINT: Check out `LEAD()` and `LAG()`
