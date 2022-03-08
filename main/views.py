from django.shortcuts import render
from django.views.generic import TemplateView

from main.constants import NumberType
from main.convertors import (
    convert_to_arabic,
    convert_to_roman,
    get_number_type,
    save_history,
)
from main.models import History


class MainPage(TemplateView):
    template_name = "main.html"

    def get(self, request, *args, **kwargs):
        history = History.objects.all()
        return render(request, self.template_name, {"history": history})

    def post(self, request):
        raw_number = request.POST.get("number").upper()

        try:
            number_type = get_number_type(raw_number)
        except ValueError as error:
            return render(
                request,
                self.template_name,
                {
                    'result': error,
                    'history': History.objects.all()
                },
            )

        if number_type == NumberType.ROMAN:
            result = convert_to_arabic(raw_number)
        else:
            result = convert_to_roman(int(raw_number))

        save_history(raw_number, result)

        args = {"result": result, "history": History.objects.all()}
        return render(request, self.template_name, args)
