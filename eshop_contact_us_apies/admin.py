from django.contrib import admin
from .models import EshopContactUs,EshopForwardContactUsMessage


class EshopContactUsAdmin(admin.ModelAdmin):
    list_display = ['read_time']

admin.site.register(EshopContactUs,EshopContactUsAdmin)
admin.site.register(EshopForwardContactUsMessage)
