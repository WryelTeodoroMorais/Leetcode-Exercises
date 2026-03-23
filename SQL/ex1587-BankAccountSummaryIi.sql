SELECT name, SUM(amount) as balance
FROM Users as U JOIN Transactions as T on U.account = T.account
GROUP BY name
HAVING SUM(amount) > 10000