#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| id            | int     |
#| recordDate    | date    |
#| temperature   | int     |
#+---------------+---------+
#id is the primary key for this table.
#This table contains information about the temperature in a certain day.
#Write an SQL query to find all dates' id with higher temperature compared to its previous dates (yesterday).

SELECT w1.id as Id
FROM Weather w1 join Weather w2 on DATE_SUB(w1.recordDate, INTERVAL 1 DAY)=w2.recordDate 
WHERE w1.temperature > w2.temperature
