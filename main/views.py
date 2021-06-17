from django.shortcuts import render
from django.views.generic import TemplateView

from . import models
from .scripts import (
    check_num,
    to_arabic,
    to_roman,
    save_history,
)


class MainPage(TemplateView):
    template_name = "main.html"

    def get(self, request):
        history = models.History.objects.all()
        args = {"history": history}

        return render(request, self.template_name, context=args)

    def post(self, request):
        # get raw string from html form and check it out
        rawNumber = request.POST.get("numStr")
        rawNumber = rawNumber.upper()
        numType = check_num(rawNumber)

        # use one of converter foo or return an error message
        if numType == None or rawNumber == "":
            res = "Incorrect input! Try again)"
        elif rawNumber == "0":
            res = 0
        elif numType == "R":
            res = to_arabic(rawNumber)
            save_history(rawNumber, res)
        elif numType == "A":
            res = to_roman(rawNumber)
            save_history(rawNumber, res)
        else:
            res = "Unexpected error! Try again)"

        # get the history of conversions
        history = models.History.objects.all()

        # create diction of arguments - result of conv. and list of history
        args = {"result": res, "history": history}

        return render(request, self.template_name, context=args)
