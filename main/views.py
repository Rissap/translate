from django.shortcuts import render
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
			"""
			save latest 6 conversion
			revrite the oldest one
			"""
			if models.History.objects.all().count() > 6:
				tmp = models.History.objects.latest()
			else:
				tmp = models.History()

			tmp.from_num = raw
			tmp.to_num = num
			tmp.time = dt.datetime.now()
			tmp.save()

		def check_num(num):
			"""
			check, is num an arabic or a roman 
			return None, if no one
			"""
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
			"""
			convert number from arabic to roman
			return string of roman numbres
			"""
			num = int(num)
			all_models = models.Numbers.objects.all()
			nums = {str(x.arabic) : x.roman for x in all_models}
			keys = list(nums.keys())

			numStr = ""

			if num//1000 > 3:
				numStr += "M*"+str(num//1000)+"+"
				num -= (num//1000)*1000

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
			"""
			convert number from roman to arabic
			return integer 
			"""
			all_models = models.Numbers.objects.all()
			nums = {str(x.roman) : x.arabic for x in all_models}
			
			num = list(num)
			calc = []
			res = 0

			#convert roman to arabic
			for x in num:
				calc.append(int(nums[x]))

			#calculate with the rules of roman number position
			for x in range(len(calc)-1):
				if calc[x] < calc[x+1]:
					calc[x] = calc[x]*(-1)

			return sum(calc)

		#get raw string from html form and check it out
		rawNumber = request.POST.get("numStr")
		rawNumber = rawNumber.upper()
		numType = check_num(rawNumber)

		#use one of converter foo or return an error message
		if numType == None or rawNumber=="":
			res = "Incorrect input! Try again)"
		elif rawNumber=="0":
			res = 0
		elif numType == "R":
			res = to_arabic(rawNumber)
			save_history(rawNumber, res)
		elif numType == "A":
			res = to_roman(rawNumber)
			save_history(rawNumber, res)
		else:
			res = "Unexpected error! Try again)"

		#get the history of conversions
		history = models.History.objects.all()

		#create diction of arguments - result of conv. and list of history
		args = {"result":res, "history":history}

		return render(request, self.template_name, context=args)
