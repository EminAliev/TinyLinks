from django.db import models


class Link(models.Model):
    full_link = models.CharField()
    short_link = models.CharField()
    redirects = models.IntegerField()
