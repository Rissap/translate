from django.shortcuts import render
from django.views.generic import TemplateView

class MainPage(TemplateView):
	template_name = "main.html"

	def get(request):
		pass

	def post(request):
		pass