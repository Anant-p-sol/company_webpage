from django.contrib import admin
from app.models import GeneralInfo

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'email', 'phone', 'open_hours')
    search_fields = ('company_name', 'location', 'email')
    list_filter = ('location',)
    ordering = ('company_name',)


    # # show the disabled and permission
    # def has_add_permission(self, request , obj=None):
    #     return False

    # # # show the disabled update permission
    # def has_change_permission(self, request, obj=None):
    #     return False

    # # # show the disabled delete permission
    # def has_delete_permission(self, request, obj=None):
    #     return False

    # # show you can set field to diable update
    rendomly_field = [
        'email'
        ]