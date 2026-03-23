SELECT name as Customers
FROM Customers
FULL JOIN Orders on Customers.id = Orders.customerID
WHERE Orders.customerID is NULL