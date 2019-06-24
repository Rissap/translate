from django.contrib import admin
from . import models

@admin.register(models.Numbers)
class AdminNumbers(admin.ModelAdmin):
	list_display = ('roman', 'arabic')