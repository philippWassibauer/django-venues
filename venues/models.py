# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

# each venue should have an own folder for images
def venueimage_get_upload_to(instance, filename):
    return "venue-images/%s/"%instance.slug
    
class VenueImage(models.Model):
    venue = models.ForeignKey('Venue', related_name="images")
    image = models.ImageField(upload_to=venueimage_get_upload_to,
                              height_field="image_height",
                              width_field="image_width")
    def __unicode__(self):                                  
        return str(self.venue)

class VenueCategory(models.Model):
    name = models.CharField(_("Category Name"), max_length=200)
    
    def __unicode__(self):                                  
        return self.name
        
class VenueCountry(models.Model):
    name = models.CharField(_("Country Name"), max_length=200)
    
    def __unicode__(self):                                  
        return self.name
    
class Venue(models.Model):
    name = models.CharField(_('name'), blank=True, max_length=100)
    creator = models.ForeignKey(User, related_name="venues")
    categories = models.ManyToManyField(VenueCategory, related_name="venues")
    phone = models.CharField(_('phone'), max_length=100, blank=True)
    address = models.CharField(_('address'), max_length=200, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)
    zip_code = models.CharField(_('zip'), blank=True, max_length=10)
    country = models.ForeignKey(VenueCountry, verbose_name=_('country'), null=True,
                                blank=True)
    about = models.TextField(_('about'), blank=True, null=True)
    website = models.CharField(_('website'), blank=True, null=True, max_length=200)
    
    PUBLIC_PRIVACY = 1
    REGISTERED_PRIVACY = 2
    PRIVACY_CHOICES = (
        (PUBLIC_PRIVACY, _('public')),
        (REGISTERED_PRIVACY, _('registered')),
    )
    
    def get_website(self):
        if self.website.find("http://") != -1:
            return self.website
        else:
            return "http://"+self.website
    