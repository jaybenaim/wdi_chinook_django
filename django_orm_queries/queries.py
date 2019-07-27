from chinook.models import *
from django.db.models import Avg, Sum, Max, Min
## 1

# Create your tests here.
Artist.objects.get(name='Queen') 
queen = Artist.objects.get(name='Queen') 
queen_albums = Album.objects.filter(artist=queen)
# 3 albums 
for album in queen_albums:  
    print(album.title)
# albums 
# Greatest Hits I
# Greatest Hits II
# News Of The World

## 2 
Track.objects.filter(media_type__name="Protected MPEG-4 video file").count()
# prints 214 

# media = MediaType.objects.filter(name="Protected MPEG-4 video file")

# prints Protected MPEG-4 video file

# count = 0 
# for item in  Track.objects.all():
#     for items in media:
#         if item.media_type.name == "Protected MPEG-4 video file": 
#             count += 1

# print(count)
   
# prints 214 

## 3 

genre = Genre.objects.filter(name="Hip Hop/Rap")
# <QuerySet [<Genre: Hip Hop/Rap>]>

for item in genre:  
    print(item.name)
# Hip Hop/Rap 



## 4
Track.objects.filter(genre__name="Hip Hop/Rap").count() 
# count = 0 
# for item in Track.objects.all(): 
#     if item.genre.name == 'Hip Hop/Rap':
#         count += 1 
# print(count)
# prints 35 

## 5 
from django.db.models import Avg, Sum, Max, Min
Track.objects.aggregate(Sum('milliseconds')) 
# {'milliseconds__sum': 1377942652}
sec = 1377942652 / 1000
mins = sec / 60 
hours = mins / 60 
days = hours / 24
print(days) 
# 15.95 days 

## 6
Track.objects.filter(media_type__name="MPEG audio file").aggregate(Max("unit_price")) 
# 'unit_price__max': Decimal('0.99')}

## 7 

Track.objects.filter(media_type__name="MPEG audio file").order_by('unit_price')[0].name
# 'Atrás Da Verd-E-Rosa Só Não Vai Quem Já Morreu'

# Track.objects.filter(media_type__name="MPEG audio file").aggregate(Max('unit_price'))
# Track.objects.order_by('-unit_price')[0].unit_price
# Track.objects.order_by('-unit_price')[0].name

## 8

Artist.objects.order_by('-created_at')[0].name
# 'Los Hermanos'
Artist.objects.order_by('-created_at')[1].name
# 'Elis Regina'

## 9 

