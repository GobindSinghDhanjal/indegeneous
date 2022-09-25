from django.contrib import admin
from asgard.models import Object

class AdminObject(admin.ModelAdmin):
    list_display = ['id','title','description']

admin.site.register(Object, AdminObject)
