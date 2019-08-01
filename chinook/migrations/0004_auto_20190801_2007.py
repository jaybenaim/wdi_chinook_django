# Generated by Django 2.2.4 on 2019-08-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0003_mediatype_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='media_types',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.MediaType'),
        ),
    ]
