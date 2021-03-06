from django.db import models

from .crf_model import CrfModel
from ..choices import RELATIONSHIP


class AdherenceCounselling(CrfModel):

    adherence_date = models.DateField(
        verbose_name='Date of Adherence Counseling',
        blank=True,
        null=True)

    adherence_partner = models.CharField(
        verbose_name='Relationship of Adherence Partner to Individual',
        max_length=25,
        blank=True,
        default=None,
        choices=RELATIONSHIP)

    adherence_partner_other = models.CharField(
        max_length=25,
        verbose_name='adherence partner: "Other"',
        blank=True,
        null=True)

    def __str__(self):
        return self.adherence_partner

    class Meta(CrfModel.Meta):
        app_label = 'ba_namotswe'
