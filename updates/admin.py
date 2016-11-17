from django.contrib import admin
from .models import Project, Subsystem, Timeline, GeneralSubsystem

# Register your models here.

admin.site.register(Project)
admin.site.register(Subsystem)
admin.site.register(Timeline)
admin.site.register(GeneralSubsystem)
