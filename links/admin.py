from django.contrib import admin
from django.contrib.admin import ModelAdmin

from links.models import Link


@admin.register(Link)
class LinkAdmin(ModelAdmin):
    list_display = ['full_link', 'short_link', 'redirects']
