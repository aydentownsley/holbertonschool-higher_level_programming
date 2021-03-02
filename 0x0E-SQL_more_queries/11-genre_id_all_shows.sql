-- SQL SCRIPT
-- LISTS ALL SHOWS WITH GENERES (EVEN IF NO GENRE)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.id ASC, tv_show_genres.genre_id;