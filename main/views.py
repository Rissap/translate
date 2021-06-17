from django.shortcuts import render
from django.views.generic import TemplateView

from . import models
from .scripts import (
    check_num,
    to_arabic,
    to_roman,
    save_history,
)
from .enums import NumberType

numberProcessMapping = {
    NumberType.ROMAN: to_arabic,
    NumberType.ARABIC: to_roman,
}


class MainPage(TemplateView):
    template_name = "main.html"

    def get(self, request):
        history = models.History.objects.all()
        return render(request, self.template_name, {"history": history})

    def post(self, request):
        raw_number = request.POST.get("numStr")
        raw_number = raw_number.upper()
        num_type = check_num(raw_number)

        if not num_type:
            return render(
                request, self.template_name, {'result': 'Unexpected input. Try again'}
            )

        result = numberProcessMapping[num_type](raw_number)

        history = models.History.objects.all()
        args = {"result": result, "history": history}

        return render(request, self.template_name, context=args)
