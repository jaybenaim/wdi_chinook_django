from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f'{self.name}'

class Album(models.Model):
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre', through='Track')
    media_types = models.ManyToManyField('MediaType', through='Track')


    def __str__(self): 
        return f'{self.title}'

class MediaType(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField('Genre', through='Track')
    albums = models.ManyToManyField(Album, through='Track')


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media_types = models.ManyToManyField('MediaType', through='Track')
    albums = models.ManyToManyField(Album, through='Track')
    
    def __str__(self):
        return f'{self.name}'

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    composer = models.CharField(max_length=255, null=True)
    milliseconds = models.IntegerField(null=False)
    bytes = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=10) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
        
class Playlist(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracks = models.ManyToManyField(Track, related_name="playlists")


