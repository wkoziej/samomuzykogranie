from django.db import models

# Create your models here.
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
 
class SongPart(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    part_order =  models.IntegerField()
    part_name = models.CharField(max_length=50)
    #instrument_setting = models.ForeignKey(InstrumentSetting, on_delete=models.CASCADE) 
    #action = models.CharField(max_length=50)
    #instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"{self.song.title} - {self.part_order} - {self.part_name}"

INSTRUMENTS = [('AMF','Arturia Micro Freak'),
               ('EMS', 'Elektron Model:Samples'),
               ('ACU', 'Acustic Guitar'),
               ('EG', 'Electric Guitar'),
               ('ZG3', 'Zoom G3')]

def get_song_part_action_object():
    return INSTRUMENTS

class SongPartAction(models.Model):
    action_order = models.IntegerField()
    song_part = models.ForeignKey(SongPart, on_delete=models.CASCADE)
    #instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)  

    action_object = models.CharField(max_length=8, choices=get_song_part_action_object())
    action_description = models.CharField(max_length=256) 
    def __str__(self):
        return f"{self.song_part}  - {self.action_order} - {self.action_object} - {self.action_description} "
