## STRETCH 
 
## 1. 
SELECT title from chinook_album WHERE artist_id in (SELECT id FROM chinook_artist WHERE name='Queen');
