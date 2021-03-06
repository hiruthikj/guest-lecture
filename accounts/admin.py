from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # fieldsets = [
    #     (
    #         "Login Info",
    #         {
    #             "fields": [
    #                 "username",
    #                 "password",
    #             ]
    #         }
    #     ),
    #     (
    #         "User Info",
    #         {
    #             "fields": [
    #                 "first_name",
    #                 "last_name",
    #                 "email",
    #                 "phone_no",
    #                 "user_type",
    #             ]
    #         },
    #     ),
    #     (
    #         "Other Info",
    #         {
    #             "fields": [
    #                 "is_staff",
    #                 "is_active",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ]
    #         },
    #     ),
    # ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('user_type', 'phone_no', )}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ('user_type', 'phone_no', )}),
    )
    list_display = ["username", "user_type", "is_staff", ]
    search_fields = ["username", ]
    list_filter = ["user_type", "is_staff", ]




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



admin.site.register(CustomUser, CustomUserAdmin)

    
