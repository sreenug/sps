from django.contrib import admin
#from forms import ImageAdminForm
from mis.models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Block)
admin.site.register(Sublocation)
admin.site.register(Village)
admin.site.register(Cluster)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(SHGProgram)
admin.site.register(AgricultureProgram)