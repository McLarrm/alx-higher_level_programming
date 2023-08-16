-- Script: List Shows with Genre IDs (Including NULL)
-- Task: List all shows from hbtn_0d_tvshows with their titles and linked genre IDs (including NULL for shows without a genre)
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
