# Table: Logs
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# id is the primary key for this table.
# Write an SQL query to find all numbers that appear at least three times consecutively.
# Return the result table in any order.


SELECT l1.num as ConsecutiveNums
FROM Logs l1 JOIN Logs l2 ON l1.Id = l2.Id-1 JOIN Logs l3 ON l3.Id-1 = l2.Id
WHERE l1.num=l2.num AND l2.num=l3.num
GROUP BY l1.num
