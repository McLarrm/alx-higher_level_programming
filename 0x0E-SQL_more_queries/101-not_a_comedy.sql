-- Script: List Shows Without Genre "Comedy"
-- Task: List all shows without the genre "Comedy" from the hbtn_0d_tvshows database
SELECT title
FROM @database_name.tv_shows
WHERE id NOT IN (
    SELECT tv_show_genres.tv_show_id
    FROM @database_name.tv_show_genres
    JOIN @database_name.tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;
