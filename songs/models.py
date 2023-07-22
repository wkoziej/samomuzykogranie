from django.db import models

# Create your models here.
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

# class Instrument(models.Model):
#     INSTRUMENTS = [('AMF','Arturia Micro Freak'),
#                    ('EMS', 'Elektron Model:Samples'),
#                    ('ZG3', 'Guitar effect Zoom G3')]
#     name = models.CharField(max_length=10, choices=INSTRUMENTS)
#     def __str__(self):
#         return self.name
    
    
# class InstrumentSetting(models.Model):
#     instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)  
#     # INSTRUMENT_PATCHES = [('BNK','Bank'),
#     #                ('PTN', 'Pattern'),
#     #                ('PTH', 'Patch'),
#     #                ('PTH', 'Patch'),
#     #                ]
    
#     # setting_name = 
#     # setting_value =
    
#     volume =  models.IntegerField(default=75)
#     settings = models.CharField(max_length=100)
#     def __str__(self):
#          return f"{self.instrument.name} - {self.volume} - {self.settings}"

# class MiccroFreakSetting (InstrumentSetting):
#     # PATTERN_CHOICES = [
#     # ('A', 'Rock'),
#     # ('B', 'Pop'),
#     # ('jazz', 'Jazz'),
#     # ('hip_hop', 'Hip Hop'),
#     # ('classical', 'Classical'),
#     # Dodaj inne gatunki muzyczne według potrzeb
#     pattern_name = models.CharField(max_length=50, choices=[(i, i) for i in "ABCDEF"])

#     def __str__(self):
#          return super().__str__() + f"{self.pattern_name}"


# class ArturiaBruteImpactSetting (InstrumentSetting):
#     # PATTERN_CHOICES = [
#     # ('A', 'Rock'),
#     # ('B', 'Pop'),
#     # ('jazz', 'Jazz'),
#     # ('hip_hop', 'Hip Hop'),
#     # ('classical', 'Classical'),
#     # Dodaj inne gatunki muzyczne według potrzeb
#     bank_name = models.CharField(max_length=50, choices=[(i, i) for i in "ABCD"])
#     tempo  = models.IntegerField()
#     def __str__(self):
#          return super().__str__() + f"{self.bank_name} - {self.tempo}"


# class GuitarZoomG3Setting (InstrumentSetting):
#     # PATTERN_CHOICES = [
#     # ('A', 'Rock'),
#     # ('B', 'Pop'),
#     # ('jazz', 'Jazz'),
#     # ('hip_hop', 'Hip Hop'),
#     # ('classical', 'Classical'),
#     # Dodaj inne gatunki muzyczne według potrzeb
#     bank_name = models.CharField(max_length=50, choices=[(i, i) for i in "ABCD"])
#     def __str__(self):
#          return super().__str__() + f"{self.bank_name} "


# class ModelSamplesSetting (InstrumentSetting):
#     # PATTERN_CHOICES = [
#     # ('A', 'Rock'),
#     # ('B', 'Pop'),
#     # ('jazz', 'Jazz'),
#     # ('hip_hop', 'Hip Hop'),
#     # ('classical', 'Classical'),
#     # Dodaj inne gatunki muzyczne według potrzeb
#     pattern_name = models.CharField(max_length=50, choices=[(i, i) for i in "ABCDEF"])
    
 
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
def get_song_part_action_name(action_object):
    action_names = [('NONE', 'No action')]
    print (action_object)
    if action_object in INSTRUMENTS:
        action_names.append(('VOL', 'Volume'))
        action_names.append(('PAT', 'Bank/Pattern'))
    return action_names

class SongPartAction(models.Model):
    action_order = models.IntegerField()
    song_part = models.ForeignKey(SongPart, on_delete=models.CASCADE)
    #instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)  

    action_object = models.CharField(max_length=8, choices=get_song_part_action_object())
    action_description = models.CharField(max_length=256) 
    def __str__(self):
        return f"{self.song_part}  - {self.action_order} - {self.action_object} - {self.action_description} "
