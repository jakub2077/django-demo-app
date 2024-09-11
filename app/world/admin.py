from django.contrib import admin
from .models import WorldBorder

class WorldBorderAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('pk', 'iso3', 'name', )

admin.site.register(WorldBorder, WorldBorderAdmin)