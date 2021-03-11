from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Event, Student, Faculty, CIRFaculty, ExternalUser, applications

admin.site.site_header = "Event Administration"
admin.site.index_title = "CRUD Operations"
admin.site.site_title = "Guest Lecture Site"

import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export as CSV"

# class CustomUserAdmin(UserAdmin):
#     fieldsets = [
#         (
#             "Login Info",
#             {
#                 "fields": [
#                     "username",
#                     "password",
#                 ]
#             }
#         ),
#         (
#             "User Info",
#             {
#                 "fields": [
#                     "first_name",
#                     "last_name",
#                     "year_of_study",
#                     "email",
#                     "phone_no",
#                 ]
#             },
#         ),
#         (
#             "Other Info",
#             {
#                 "fields": [
#                     "is_staff",
#                     "is_active",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ]
#             },
#         ),
#     ]
#     # inlines = [UserInline]
#     list_display = ["username", "dept_fk", "year_of_study"]
#     list_filter = ["dept_fk__dept_code"]

#     search_fields = ["username"]


# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(CIRFaculty)
admin.site.register(ExternalUser)
admin.site.register(applications)
admin.site.register(Event)
