from django.contrib import admin
from .models import Technology, Project, Recognition, ContactMessage, Resume
from import_export.admin import ImportExportModelAdmin

class TechnologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Technology, TechnologyAdmin)

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'order_number', 'is_active']

admin.site.register(Project, ProjectAdmin)

class RecognitionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'is_active', 'tag']

admin.site.register(Recognition, RecognitionAdmin)

class ContactMessageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

admin.site.register(ContactMessage, ContactMessageAdmin)

class ResumeAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ['link']

admin.site.register(Resume, ResumeAdmin)