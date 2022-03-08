from django.shortcuts import render
from django.views.generic import TemplateView

from . import models
from main.convertors import (
    get_number_type,
    convert_to_arabic,
    convert_to_roman,
    save_history,
)
from main.constants import NumberType


class MainPage(TemplateView):
    template_name = "main.html"

    def get(self, request):
        history = models.History.objects.all()
        return render(request, self.template_name, {"history": history})

    def post(self, request):
        raw_number = request.POST.get("number")
        raw_number = raw_number.upper()
        num_type = get_number_type(raw_number)

        if not num_type:
            return render(
                request, self.template_name, {'result': 'Unexpected input. Try again'}
            )

        if num_type == NumberType.ROMAN:
            result = convert_to_arabic(raw_number)
        else:
            result = convert_to_roman(int(raw_number))

        history = models.History.objects.all()
        args = {"result": result, "history": history}

        return render(request, self.template_name, args)
