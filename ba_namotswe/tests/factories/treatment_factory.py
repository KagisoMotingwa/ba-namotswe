import factory

from datetime import date
from ba_namotswe.models import Treatment
from edc_constants.constants import YES


class TreatmentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Treatment

    perinatal_infection = 'tb',

    pmtct = YES

    pmtct_rx = 'AZT Monotherapy'

    infant_prohylaxis = YES

    infant_prohylaxis_rx = 'AZT'

    counseling = 'session'

    adherence_partner_rel = 'mother'

    adherence_partner_rel_other = None