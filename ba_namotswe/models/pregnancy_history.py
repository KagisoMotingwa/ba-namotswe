from django.db import models

from .crf_model import CrfModel
from ..choices import PREGNANCY


class PregnancyHistory(CrfModel):

    class Meta(CrfModel.Meta):
        app_label = 'ba_namotswe'
