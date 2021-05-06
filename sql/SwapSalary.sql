# Table: Salary
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id is the primary key for this table.
# The sex column is ENUM value of type ('m', 'f').
# The table contains information about an employee.

# Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) 
# with a single update statement and no intermediate temp table(s).

UPDATE Salary
SET sex = IF(sex='f', 'm', 'f')
