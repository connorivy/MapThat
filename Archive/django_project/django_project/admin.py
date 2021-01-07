from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as pisces_models


admin.site.register(pisces_models.spots, LeafletGeoAdmin)
