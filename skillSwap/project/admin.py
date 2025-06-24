from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technologies', 'start_date')
    
admin.site.register(Project, ProjectAdmin)
