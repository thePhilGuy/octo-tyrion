from django.contrib import admin
from mini_url.models import Mini

class MiniAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'date', 'author', 'counter')
    list_filer = ('author')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('long_url',)
    
admin.site.register(Mini, MiniAdmin)