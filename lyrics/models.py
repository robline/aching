from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    writers = models.TextField()

    def __str__(self):
        return self.title

class Verse(models.Model):
    verse_text = models.TextField()
    song = models.ForeignKey(Song)

    def __str__(self):
        return "Verse from {}".format(self.song.title)
