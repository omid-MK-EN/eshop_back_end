from django.contrib import admin
from .models import EshopContactUs,EshopForwardContactUsMessage,EshopSocialMedia


class EshopContactUsAdmin(admin.ModelAdmin):
    list_display = ['read_time']

admin.site.register(EshopContactUs,EshopContactUsAdmin)
admin.site.register(EshopForwardContactUsMessage)
admin.site.register(EshopSocialMedia)
