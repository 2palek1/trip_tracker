from django.contrib import admin

from trip.models import Trip, Note

# Register your models here.
admin.site.register(Trip)
admin.site.register(Note)