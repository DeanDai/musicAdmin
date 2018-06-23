from django.contrib import admin
from music.models import Song 

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'pub_time')
    list_filter = ('pub_time',)
admin.site.register(Song, SongAdmin)