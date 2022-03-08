from django.db import models
from django.conf import settings


class History(models.Model):
    convert_from = models.CharField(max_length=128)
    convert_to = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def date(self):
        return self.created_at.strftime(settings.HISTORY_DATE_FORMAT)

    class Meta:
        ordering = ["-created_at"]
