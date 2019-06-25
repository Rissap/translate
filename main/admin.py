from django.contrib import admin
from . import models

@admin.register(models.Numbers)
class AdminNumbers(admin.ModelAdmin):
	list_display = ('roman', 'arabic')

@admin.register(models.History)
class AdminHistory(admin.ModelAdmin):
	list_display = ('from_num', 'to_num', 'time')