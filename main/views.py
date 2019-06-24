from django.shortcuts import render
from django.views.generic import TemplateView

class MainPage(TemplateView):
	template_name = "main.html"

	args = {}

	def get(self, request):
		return render(request, self.template_name, {"args":self.args})

	def post(self, request):
		pass