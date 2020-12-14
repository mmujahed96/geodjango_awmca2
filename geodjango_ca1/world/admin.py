from django.contrib.gis import admin
from .models import WorldBorder, Locations

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Locations, admin.GeoModelAdmin)