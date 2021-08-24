from bloom.serializers import ContactSerializer
from django.contrib import admin
from .models import Activity, Opportunity, Contact, Company

# Register your models here.

admin.site.register(Activity)
admin.site.register(Opportunity)
admin.site.register(Contact)
admin.site.register(Company)
