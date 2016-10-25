from .crf_model import CrfModel
from django.db import models
from ba_namotswe.models.transfer_history import TransferHistory


class Transfer(CrfModel):

    transfer = models.ForeignKey(TransferHistory)

    transfer_date = models.DateField()

    transfer_reason = models.CharField(max_length=100)

    class Meta(CrfModel.Meta):
        app_label = 'ba_namotswe'
