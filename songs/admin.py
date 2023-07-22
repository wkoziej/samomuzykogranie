from django.contrib import admin

# Register your models here.
from .models import Song, SongPart, SongPartAction#, MiccroFreakSetting, ArturiaBruteImpactSetting, ModelSamplesSetting, GuitarZoomG3Setting
admin.site.register(Song)
admin.site.register(SongPart)
admin.site.register(SongPartAction)

# admin.site.register(ArturiaBruteImpactSetting)
# admin.site.register(ModelSamplesSetting)
# admin.site.register(GuitarZoomG3Setting)