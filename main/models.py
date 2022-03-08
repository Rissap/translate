from django.db import models
from django.conf import settings


class HistoryLimitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()[:settings.HISTORY_ITEMS_LIMIT]


class History(models.Model):
    convert_from = models.CharField(max_length=128)
    convert_to = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    latest = HistoryLimitManager()

    @property
    def date(self):
        return self.created_at.strftime(settings.HISTORY_DATE_FORMAT)

    class Meta:
        ordering = ["-created_at"]
