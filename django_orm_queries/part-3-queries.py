
1. Track.objects.filter(album__title="Vinicius De Moraes")   
2. Album.objects.filter(artist__name="Philip Glass Ensemble")    
3. Track.objects.filter(playlists__name="Brazilian Music") 
4. Track.objects.filter(genre__name='Jazz')
5. Genre.objects.filter(track__name='My Time After Awhile') 
6.  media =  MediaType.objects.filter(track__name="My Time After Awhile") 
    for name in media: 
        print(name.name) 
7. Album.objects.filter(artist__name="My Time After Awhile")

