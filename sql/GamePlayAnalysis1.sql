# Table: Activity
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key of this table.
# This table shows the activity of players of some game.
# Each row is a record of a player who logged in and played a number of games 
# (possibly 0) before logging out on some day using some device.
#
# Write an SQL query that reports the first login date for each player.
# The query result format is in the following example:
# 
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-05-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id

# Explanation: We clearly want the player_id and the event_date columns. 
# Thus, it makes sense to start with SELECT player_id, event_date FROM Activity
# However, we want the very first login date, so let's change that to: 
# SELECT player_id, MIN(event_date) AS first_login FROM Activity
# Let's rename the MIN() field to first_login to be a little clearer.
# You might think that should get the very first date, just like we want,
# But there's a problem. MIN() is a type of aggregation, meaning SQL
# Is combining the result set from our query somehow. Our problem is that
# SQL doesn't know HOW to do the combining. Should it be the MIN()
# For each device_id? For each player_id? It's ambiguous to SQL. 
# So, with this: SELECT player_id, MIN(event_date) AS first_login 
#                FROM Activity
#                GROUP BY player_id
# We eliminate the ambiguity and tell SQL we want the minimum for each player. 
