from django.contrib import admin
from .models import Project, ProjectMember

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectMember)