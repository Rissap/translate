from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

import datetime as dt

from . import models

class MainPage(TemplateView):
	template_name = "main.html"

	def get(self, request):
		history = models.History.objects.all()
		args = {"history":history}
		
		return render(request, self.template_name, context=args)

	def post(self, request):

		def save_history(raw, num):
			
			if models.History.objects.all().count() > 6:
				tmp = models.History.objects.latest()
			else:
				tmp = models.History()

			tmp.from_num = raw
			tmp.to_num = num
			tmp.time = dt.datetime.now()
			tmp.save()

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

		if numType == None or rawNumber=="":
			res = "Incorect input! Try again)"
		elif numType == "R":
			res = to_arabic(rawNumber)
			save_history(rawNumber, res)
		elif numType == "A":
			res = to_roman(rawNumber)
			save_history(rawNumber, res)
		else:
			res = "Unexpected error! Try again)"

		history = models.History.objects.all()

		args = {"result":res, "history":history}

		return render(request, self.template_name, context=args)
