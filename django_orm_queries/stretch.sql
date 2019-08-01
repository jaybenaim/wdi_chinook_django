## STRETCH 
 
## 1. 
SELECT title from chinook_album WHERE artist_id in (SELECT id FROM chinook_artist WHERE name='Queen');                                                                                                                   
+-------------------+
| title             |
|-------------------|
| Greatest Hits I   |
| Greatest Hits II  |
| News Of The World |
+-------------------+


## 2 
SELECT COUNT(name) FROM chinook_track where media_type_id in (SELECT id FROM chinook_mediatype where name='Protected MPEG-4 video file');                                                                                
+---------+
| count   |
|---------|
| 214     |
+---------+

# 3 
SELECT name from chinook_track where genre_id in (SELECT id from chinook_genre where name='Electronica/Dance') ORDER BY unit_price ASC LIMIT 1; 
+--------------------+
| name               |
|--------------------|
| Instinto Colectivo |
+--------------------+

# 4 
SELECT NAME FROM chinook_artist WHERE name LIKE 'A%'; 
+---------------------------------------------------------------------------------------+
| name                                                                                  |
|---------------------------------------------------------------------------------------|
| Aquaman                                                                               |
| AC/DC                                                                                 |
| Alanis Morissette                                                                     |
| Audioslave                                                                            |
SELECT 26 

# 5 

select * from chinook_playlist_tracks where playlist_id=1;

+------+---------------+------------+
| id   | playlist_id   | track_id   |
|------+---------------+------------|
| 3285 | 1             | 3499       |
| 3284 | 1             | 3498       |
| 3283 | 1             | 3497       |
| 3282 | 1             | 3496       |
| 3281 | 1             | 3495       |
SELECT 3285

