from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import History
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
        history = History.objects.all()
        return render(request, self.template_name, {"history": history})

    def post(self, request):
        raw_number = request.POST.get("number")
        raw_number = raw_number.upper()
        number_type = get_number_type(raw_number)

        if not number_type or not raw_number:
            return render(
                request, 
                self.template_name, 
                {
                    'result': 'Unexpected input. Try again',
                    'history': History.objects.all()
                }, 
            )

        if number_type == NumberType.ROMAN:
            result = convert_to_arabic(raw_number)
        else:
            result = convert_to_roman(int(raw_number))

        save_history(raw_number, result)
        history = History.objects.all()
        args = {"result": result, "history": history}

        return render(request, self.template_name, args)
