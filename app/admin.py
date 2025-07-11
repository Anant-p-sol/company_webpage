from django.contrib import admin
from app.models import (
    GeneralInfo,
    Service ,
    Testinomial,
    FrequentlyAskedQuestion,
    )

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
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("tittle", "description")



    search_fields = ("tittle", "description")

@admin.register(Testinomial)
class TestinomialAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_job_title", "display_rating_count")


    def display_rating_count(self, obj):
        return "*" * obj.rating_count
    display_rating_count.short_description = "Rating"

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "answer",]


    