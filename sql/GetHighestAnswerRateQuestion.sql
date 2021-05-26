# Get the highest answer rate question from a table survey_log with these columns: 
# id, action, question_id, answer_id, q_num, timestamp.
# id means user id; action has these kind of values: "show", "answer", "skip"; 
# answer_id is not null when action column is "answer", while is null for "show" and "skip";
# q_num is the numeral order of the question in current session.
# 
# Write a sql query to identify the question which has the highest answer rate.
# 
# Example:
#   Input:
# +------+-----------+--------------+------------+-----------+------------+
# | id   | action    | question_id  | answer_id  | q_num     | timestamp  |
# +------+-----------+--------------+------------+-----------+------------+
# | 5    | show      | 285          | null       | 1         | 123        |
# | 5    | answer    | 285          | 124124     | 1         | 124        |
# | 5    | show      | 369          | null       | 2         | 125        |
# | 5    | skip      | 369          | null       | 2         | 126        |
# +------+-----------+--------------+------------+-----------+------------+
#  Output:
# +-------------+
# | survey_log  |
# +-------------+
# |    285      |
# +-------------+
# Explanation:
# question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.

WITH cte1 AS 
    ( SELECT question_id, COUNT(answer_id) AS counts
    FROM survey_log
    GROUP BY question_id )

SELECT question_id AS survey_log 
FROM cte1
ORDER BY counts DESC
LIMIT 1

# The built-in aggregation function COUNT() doesn't count NULL entries. Therefore,
# we just need to count the number of answer_id appearances per question_id,
# then order the results by the count and take only the top entry. 
