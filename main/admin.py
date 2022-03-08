from django.contrib import admin

from main.models import History


@admin.register(History)
class AdminHistory(admin.ModelAdmin):
	list_display = ('convert_from', 'convert_to', 'date')
