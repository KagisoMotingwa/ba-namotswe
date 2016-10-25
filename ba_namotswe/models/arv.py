from .crf_model import CrfModel
from django.db import models
from ba_namotswe.models.arv_history import ArvHistory


class Arv(CrfModel):

    arv = models.ForeignKey(ArvHistory)

    name = models.CharField(max_length=30)

    date_started = models.DateField()

    date_end = models.DateField()

    reason = models.CharField(max_length=100)

    class Meta(CrfModel.Meta):
        app_label = 'ba_namotswe'
        verbose_name = 'ARV'
