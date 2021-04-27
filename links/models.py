from django.db import models


class Link(models.Model):
    full_link = models.CharField(max_length=200)
    short_link = models.CharField(max_length=50, unique=True)
    redirects = models.IntegerField(default=0)

    def __str__(self):
        return self.short_link
