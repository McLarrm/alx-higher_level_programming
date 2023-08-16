-- Script: List Genres Not Linked to Show "Dexter"
-- Task: List all genres not linked to the show "Dexter" from the hbtn_0d_tvshows database
SELECT name
FROM @database_name.tv_genres
WHERE id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM @database_name.tv_show_genres
    JOIN @database_name.tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
