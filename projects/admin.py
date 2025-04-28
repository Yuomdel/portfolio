from django.contrib import admin
from projects.models import Skill, Project


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'order')
    list_editable = ('percentage', 'order')

admin.site.register(Skill, SkillAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'order')
    list_filter = ('date_created',)
    search_fields = ('title', 'description')
    list_editable = ('order',)
    filter_horizontal = ('technology',)
    
admin.site.register(Project, ProjectAdmin)