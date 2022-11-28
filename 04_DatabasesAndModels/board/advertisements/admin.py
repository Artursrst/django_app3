from django.contrib import admin
from .models import Advertisement, AuthorInformation, Headings

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthorInformation)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Headings)
class HeadingsAdmin(admin.ModelAdmin):
    pass