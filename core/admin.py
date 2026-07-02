from django.contrib import admin
from .models import Technology, Project, Recognition, ContactMessage, Resume
from import_export.admin import ImportExportActionModelAdmin

class TechnologyAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Technology, TechnologyAdmin)

class ProjectAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'is_active']

admin.site.register(Project, ProjectAdmin)

class RecognitionAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'is_active', 'tag']

admin.site.register(Recognition, RecognitionAdmin)

class ContactMessageAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

admin.site.register(ContactMessage, ContactMessageAdmin)

class ResumeAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    list_display = ['link']

admin.site.register(Resume, ResumeAdmin)