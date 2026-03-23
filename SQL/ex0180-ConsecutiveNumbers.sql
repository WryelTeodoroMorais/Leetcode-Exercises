SELECT DISTINCT L1.num as ConsecutiveNums
FROM Logs as L1, Logs as L2, Logs as L3
WHERE L1.id = L2.id + 1 and L1.id = L3.id + 2 
and L1.num = L2. num and L1.num = L3.num 