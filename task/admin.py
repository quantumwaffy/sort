from django.contrib import admin
from .models import SortedData



class SortedAdmin(admin.ModelAdmin):
    list_display = ('kind','beforesort','aftersort', 'exectime','timestart')
    list_display_links = ('beforesort','aftersort', 'exectime','timestart')
    search_fields = ('kind','exectime')
    ordering = ('kind','exectime')



admin.site.register(SortedData,SortedAdmin)