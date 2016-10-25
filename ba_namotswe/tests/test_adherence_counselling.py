from datetime import date
from django.test import TestCase

from edc_constants.constants import YES

from ba_namotswe.forms.adherence_counselling_form import AdherencePartnerRelationForm
from ba_namotswe.tests.factories.adherence_counselling_factory import AdherenceCounsellingFactory


class TestAdherencePartnerRelationForm(TestCase):

    def setUp(self):
        self.adherencepartnerrelationForm = AdherenceCounsellingFactory
        self.data = {
            'adherence_date': date(2016, 10, 14),
            'adherence_partner': 'uncle',
            'adherence_partner_other': None}

    def test_valid_form(self):
        """Test to verify whether form will submit"""
        form = AdherencePartnerRelationForm(data=self.data)
        self.assertTrue(form.is_valid())
