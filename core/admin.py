from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserProfile)
admin.site.register(Superadmin)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Agent)
admin.site.register(CustomerCare)
