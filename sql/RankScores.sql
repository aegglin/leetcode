# +----+-------+
# | Id | Score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+
# Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. 
# Note that after a tie, the next ranking number should be the next consecutive integer value.
# In other words, there should be no "holes" between ranks.


SELECT Score, DENSE_RANK() OVER(
    ORDER BY Score DESC
) AS 'Rank'
FROM Scores
