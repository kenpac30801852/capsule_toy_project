from django.contrib import admin
from .models import CapsuleToy

class CapsuleToyAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price')
    search_fields = ('name', 'manufacturer')
    fields = ('name', 'release_date', 'price', 'manufacturer', 'url', 'image_url', 'description')

admin.site.register(CapsuleToy, CapsuleToyAdmin)
