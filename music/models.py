from django.db import models

# Create your models here.
from AudioArtistry.models import TimestampedUUIDModel



class Music(TimestampedUUIDModel):
    serial_num = models.IntegerField(default=0)
    music = models.FileField(null=True,blank=True,upload_to='media/')

class MusicImage(TimestampedUUIDModel):
    image = models.FileField(null=True,blank=True,upload_to='media/')
    merge_music = models.FileField(null=True,blank=True,upload_to='media/')
    latitude = models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=6)
    longitude = models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=6)

