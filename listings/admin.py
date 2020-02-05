from django.contrib import admin

from .models import Listing

class LisitngAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('list_date',)
    list_editable = ('is_published',)
    search_fields = ('price','address','realtor')


admin.site.register(Listing,LisitngAdmin)
