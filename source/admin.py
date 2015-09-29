from django.contrib import admin 

from .models import Person, Sign 
#brings person and sign into the admin portal
admin.site.register(Person)
admin.site.register(Sign)
