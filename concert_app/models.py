from django.db import models

class ArtistSearch(models.Model):
    artist_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}, {self.artist_name}"