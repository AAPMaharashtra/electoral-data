from django.contrib import admin

# Register your models here.
from electoral_data.models import LokSabhaSeat
from electoral_data.models import AssemblyConstituency
from electoral_data.models import PollingStation
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from electoral_data.models import UserProfile

admin.site.register(LokSabhaSeat)
admin.site.register(AssemblyConstituency)
admin.site.register(PollingStation)

class UserProfileInline(admin.TabularInline):
	model = UserProfile


class MyUserAdmin(UserAdmin):
	inlines = [
		UserProfileInline
	]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)