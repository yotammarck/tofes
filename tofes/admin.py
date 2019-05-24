from django.contrib import admin
from .models import Right, Entry

# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','created','input_age')
    search_fields = ['first_name', 'last_name']
    list_filter = ['input_age']
admin.site.register(Right)
admin.site.register(Entry, EntryAdmin)
