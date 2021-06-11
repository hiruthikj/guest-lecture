from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Department, Event, Student, Faculty, CIRFaculty, ExternalUser, applications, Guest

User = get_user_model()

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
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export as CSV"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = [
        ('Event Info',         {'fields': ['event_name','start_date','end_date','guest_fk', 'occupied_seats','max_seats', 'allow_ext']}),
        ('Other Info',       {'fields': ['description','summary','place','status','type', 'created_by',]}),
    ]
    # inlines = [ChoiceInline]
    list_display = ['event_name','start_date','end_date','type','occupied_seats','max_seats', 'status' ]  
    list_filter = ['status','type','start_date','end_date', 'guest_fk']
    ordering = ['end_date', ]
    
    search_fields = ['event_name', ]
    readonly_fields = ('created_by','occupied_seats')

    actions = ["export_as_csv",]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(EventAdmin, self).save_model(request, obj, form, change)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin, ExportCsvMixin):

    list_display = ['account','dept_fk',]  
    list_filter = ['dept_fk', ]
    
    search_fields = ['account__username', ]
    # readonly_fields = ('created_by',)

    actions = ["export_as_csv",]

    def save_model(self, request, obj, form, change):
        user = User.objects.get(id=obj.account.id)
        user.is_staff = True

        faculty_group = Group.objects.get(name='FacultyGroup') 
        user.groups.add(faculty_group)
        # faculty_group.user_set.add(your_user)

        user.save()
        super().save_model(request, obj, form, change)


@admin.register(CIRFaculty)
class CIRFacultyAdmin(admin.ModelAdmin, ExportCsvMixin):

    list_display = ['account']  
    
    search_fields = ['account__username', ]

    actions = ["export_as_csv",]

    def save_model(self, request, obj, form, change):
        user = User.objects.get(id=obj.account.id)
        user.is_staff = True

        cir_faculty_group = Group.objects.get(name='CIRFacultyGroup') 
        user.groups.add(cir_faculty_group)
        # faculty_group.user_set.add(your_user)

        user.save()
        super().save_model(request, obj, form, change)



@admin.register(applications)
class ApplicationAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['event', 'student', ]  
    list_filter = ['event', 'student', ]
    
    search_fields = ['event__event_name' ]
    readonly_fields = ('event', 'student', )

    actions = ["export_as_csv",]

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['account', ]  
    # list_filter = ['event', 'student', ]
    
    search_fields = ['account__username' ]
    # readonly_fields = ('event', 'student', )

    actions = ["export_as_csv",]

# admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['dept_code', 'dept_name']  
    # list_filter = ['event', 'student', ]
    
    search_fields = ['dept_name' ]
    # readonly_fields = ('event', 'student', )

    actions = ["export_as_csv",]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['account', 'reg_no']  
    # list_filter = ['event', 'student', ]
    
    search_fields = ['account__username', ]
    # readonly_fields = ('event', 'student', )

    actions = ["export_as_csv",]



@admin.register(ExternalUser)
class ExternalUserAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['account',]  
    # list_filter = ['event', 'student', ]
    
    search_fields = ['account__username', ]
    # readonly_fields = ('event', 'student', )

    actions = ["export_as_csv",]
