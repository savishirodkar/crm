from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Superadmin)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Agent)
admin.site.register(CustomerCare)
admin.site.register(Escalators)
admin.site.register(TeamManager)
admin.site.register(TeamLead)

