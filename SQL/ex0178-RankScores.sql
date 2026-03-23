SELECT S.score, (SELECT COUNT (DISTINCT S1.score) FROM Scores as S1
WHERE S1.score >= S.score) as rank
FROM Scores as S
ORDER BY S.score DESC