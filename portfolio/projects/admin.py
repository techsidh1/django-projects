from django.contrib import admin
from .models import Project, Person, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title',)
    search_fields= ('title',)


class ProjectAdmin(admin.ModelAdmin):
    list_display =('title', 'github_link')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Person)
admin.site.register(Blog, BlogAdmin)
