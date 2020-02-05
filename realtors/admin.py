from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    search_fields = ('name',)
    list_per_page = 25
    list_filter = ('name',)


admin.site.register(Realtor,RealtorAdmin)
