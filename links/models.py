from django.db import models


class Link(models.Model):
    full_link = models.CharField()
    short_link = models.CharField()
    redirects = models.IntegerField()

    def __str__(self):
        return self.short_link
