-- lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.

SELECT tg.name AS genre, COUNT(tsg.genre_id) AS `number_of_shows`
FROM `tv_genres` tg
JOIN `tv_show_genres` tsg
ON tg.id = tsg.genre_id
GROUP BY tg.name
HAVING `number_of_shows` > 0
ORDER BY `number_of_shows` DESC;
