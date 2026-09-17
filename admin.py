from django.contrib import admin  # type: ignore[reportMissingModuleSource]
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'salary',
                    'posted_by', 'date_posted')
    search_fields = ('title', 'company_name')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'date_applied')


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
