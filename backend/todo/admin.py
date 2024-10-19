from django.contrib import admin
from . import models
# Register your models here.

class TodAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed']

    def _str_(self):
        return self.title

admin.site.register(models.Todo)
