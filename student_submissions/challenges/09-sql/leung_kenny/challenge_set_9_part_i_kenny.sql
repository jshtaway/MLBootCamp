#Question 1
SELECT CustomerName 
FROM Customers
WHERE Country = 'UK';

#Question 2
SELECT CustomerName, COUNT(*)
FROM Customers
JOIN Orders 
ON Customers.CustomerID = Orders.CustomerID 
GROUP BY CustomerName 
ORDER BY COUNT(*) DESC
LIMIT 1;

#Question 3
SELECT SupplierName, AVG(Price)
FROM Suppliers
JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
ORDER BY AVG(Price) DESC
LIMIT 1;

#Question 4
SELECT COUNT(DISTINCT(Country)) AS DiffCountries 
FROM Customers;

#Question 5
SELECT CategoryName, COUNT(*) FROM OrderDetails
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
JOIN Categories
On Products.CategoryID = Categories.CategoryID
GROUP BY CategoryName
ORDER BY COUNT(*) DESC
LIMIT 1;

#Question 6
SELECT OrderID, SUM(Quantity*Price) AS TotalPrice 
FROM OrderDetails
JOIN Products
ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderID;

#Question 7
SELECT LastName, FirstName, TotalSales FROM Employees
JOIN (SELECT EmployeeID, SUM(TotalPrice) AS TotalSales FROM Orders
	JOIN (SELECT OrderID, SUM(Quantity*Price) AS TotalPrice 
		FROM OrderDetails
		JOIN Products
		ON OrderDetails.ProductID = Products.ProductID
		GROUP BY OrderID)
GROUP BY EmployeeID) a
ON Employees.EmployeeID = a.EmployeeID;

#Question 8
SELECT LastName, FirstName, Notes FROM Employees
WHERE Notes LIKE '% BS %';

#Question 9
SELECT SupplierName, Average FROM Suppliers
JOIN (SELECT SupplierID, SUM(Price)/COUNT(SupplierID) AS Average 
FROM Products
GROUP BY SupplierID
HAVING COUNT(SupplierID) > 2) a
ON Suppliers.SupplierID = a.SupplierID
ORDER BY Average DESC
LIMIT 1;