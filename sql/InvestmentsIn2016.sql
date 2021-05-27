WITH tiv_counts AS 
(SELECT TIV_2015, COUNT(TIV_2015) AS 2015_counts
FROM insurance
GROUP BY TIV_2015
HAVING 2015_counts > 1), 

map_freqs AS 
(SELECT TIV_2015, TIV_2016, COUNT(LAT) AS lat_freqs, COUNT(LON) AS lon_freqs
FROM insurance
GROUP BY LAT, LON
HAVING lat_freqs <= 1 AND lon_freqs <= 1)

SELECT SUM(map_freqs.TIV_2016) AS TIV_2016
FROM tiv_counts JOIN map_freqs ON tiv_counts.TIV_2015 = map_freqs.TIV_2015
