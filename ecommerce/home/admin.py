from django.contrib import admin

# Register your models here.

from home.models import HomeDetails,QuoteDetails, ContactDetailsTable

admin.site.register(HomeDetails)
admin.site.register(QuoteDetails)
admin.site.register(ContactDetailsTable)