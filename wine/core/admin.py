from django.contrib import admin
from .models import UserProfile, Wine, Review

admin.site.register(UserProfile)
admin.site.register(Wine)
admin.site.register(Review)
