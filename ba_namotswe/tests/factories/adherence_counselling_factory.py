import factory

from datetime import date
from edc_constants.constants import YES
from ba_namotswe.models.adherence_counselling import Adherence_Counselling


class AdherenceCounsellingFactory(factory.DjangoModelFactory):

    class Meta:
        model = Adherence_Counselling

    adherence_date = date(2016, 10, 14)

    adherence_partner = 'uncle'

    adherence_partner_other = None
