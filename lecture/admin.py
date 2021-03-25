from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Event, Student, Faculty, CIRFaculty, ExternalUser, applications

admin.site.site_header = "Event Administration"
admin.site.index_title = "CRUD Operations"
admin.site.site_title = "Lecture Site"

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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = [
        ('Event Info',         {'fields': ['event_name','start_date','end_date','max_seats']}),
        ('Other Info',       {'fields': ['description','summary','place','status','type', 'created_by',]}),
    ]
    # inlines = [ChoiceInline]
    list_display = ['event_name','start_date','end_date','type','status', ]  
    list_filter = ['status','type','start_date','end_date', ]
    
    search_fields = ['event_name', ]
    readonly_fields = ('created_by',)

    actions = ["export_as_csv",]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(EventAdmin, self).save_model(request, obj, form, change)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin, ExportCsvMixin):

    list_display = ['account','dept_fk',]  
    list_filter = ['dept_fk', ]
    
    search_fields = ['account__first_name', ]
    # readonly_fields = ('created_by',)

    actions = ["export_as_csv",]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(EventAdmin, self).save_model(request, obj, form, change)

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
# admin.site.register(Faculty)
admin.site.register(CIRFaculty)
admin.site.register(ExternalUser)
admin.site.register(applications)
# admin.site.register(Event, EventAdmin)
