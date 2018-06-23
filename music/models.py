from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=32, default='title')
    artist = models.CharField(max_length=32)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title