from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import models

class MainPage(TemplateView):
	template_name = "main.html"

	args = {"result":"nothing"}

	def get(self, request):
		return render(request, self.template_name, {"result": "none"})

	def post(self, request):

		def check_num(num):
			all_models = models.Numbers.objects.all()
			roman = [x.roman for x in all_models]
			arabic = [str(x) for x in range(10)]
			
			num = list(num)

			if set(num).issubset(roman):
				return "R"

			elif set(num).issubset(arabic):
				return "A"

			else:
				return None



		def to_roman(num):

			num = int(num)
			all_models = models.Numbers.objects.all()
			nums = {str(x.arabic) : x.roman for x in all_models}
			keys = list(nums.keys())

			numStr = ""
			for x in range(len(keys)):
				amount = num // int(keys[x])

				if amount > 3 and int(keys[x])!=1000:
					numStr += nums[keys[x]] + nums[keys[x-1]]
					num = num - (int(keys[x-1]) - int(keys[x]))

				else:
					for j in range(amount):
						numStr += nums[keys[x]]
					num = num - amount*int(keys[x])

			return numStr

		def to_arabic(num):

			all_models = models.Numbers.objects.all()
			nums = {str(x.roman) : x.arabic for x in all_models}
			
			num = list(num)
			calc = []
			res = 0

			for x in num:
				calc.append(int(nums[x]))

			for x in range(len(calc)-1):
				if calc[x] < calc[x+1]:
					calc[x] = calc[x]*(-1)

			return sum(calc)

		

		rawNumber = request.POST.get("numStr")
		numType = check_num(rawNumber)

		if numType == None:
			res = "Incorect input! Try again)"
		elif numType == "R":
			res = to_arabic(rawNumber)
		elif numType == "A":
			res = to_roman(rawNumber)
		else:
			res = "Unexpected error! Try again)"

		args = {"result":res}

		return render(request, self.template_name, context=args)
