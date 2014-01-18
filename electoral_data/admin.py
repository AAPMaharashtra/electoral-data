from django.contrib import admin

# Register your models here.
from electoral_data.models import LokSabhaSeat
from electoral_data.models import AssemblyConstituency
from electoral_data.models import PollingStation
from electoral_data.models import Society

admin.site.register(LokSabhaSeat)
admin.site.register(AssemblyConstituency)
admin.site.register(PollingStation)
admin.site.register(Society)
