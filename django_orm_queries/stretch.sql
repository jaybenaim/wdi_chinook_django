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

