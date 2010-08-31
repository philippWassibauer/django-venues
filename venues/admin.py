#!/usr/bin/env python
from models import *
from django.contrib import admin

class VenueImageInline(admin.TabularInline):
    model = VenueImage
    
class VenueAdmin(admin.ModelAdmin):
    list_display        = ('name', 'address', 'city', 'zip_code', "country", "creator")
    list_filter         = ('name', 'country', "city", "zip_code", "creator")
    search_fields       = ('name', 'country')
    
    inlines = [
        VenueImageInline,
    ]
    
admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueImage)
admin.site.register(VenueCategory)
