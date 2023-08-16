-- Script: List Genres by Rating Sum
-- Task: List all genres in the hbtn_0d_tvshows_rate database by their rating sum
SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating_sum
FROM @database_name.tv_genres
LEFT JOIN @database_name.tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN @database_name.tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
