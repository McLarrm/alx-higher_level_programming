-- Script: List Shows by Rating Sum
-- Task: List all shows from hbtn_0d_tvshows_rate by their rating sum
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM @database_name.tv_shows
LEFT JOIN @database_name.tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
