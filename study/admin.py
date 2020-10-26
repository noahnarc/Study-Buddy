from django.contrib import admin

from .models import Profile, StudyGroup

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)


class StudyGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudyGroup, StudyGroupAdmin)

