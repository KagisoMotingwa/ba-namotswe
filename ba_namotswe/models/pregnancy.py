from .crf_model import CrfModel
from django.db import models
from ba_namotswe.models.pregnancy_history import PregnancyHistory


class Pregnancy(CrfModel):

    pregnancy = models.ForeignKey(PregnancyHistory)

    first_documentation_of_Pregnancy_date = models.DateField()

    delivery_date = models.DateField()

    class Meta(CrfModel.Meta):
        app_label = 'ba_namotswe'
