from datetime import date
from django.test import TestCase

from edc_constants.constants import YES

from ba_namotswe.forms.treatment_form import TreatmentForm
from ba_namotswe.tests.factories.treatment_factory import TreatmentFactory


class TestTreatmentForm(TestCase):

    def setUp(self):
        """Setup data with all required fields for Treatment"""
        self.treatment = TreatmentFactory
        self.data = {
            'report_date': date(2016,10,13),
            'perinatal_infection': YES,
            'pmtct': YES,
            'pmtct_rx': 'AZT Monotherapy',
            'infant_prohylaxis': YES,
            'infant_prohylaxis_rx': 'AZT',
            'counseling': YES,
            'counseling_date': date(2016, 7, 7),
            'adherence_partner_rel': 'Mother',
            'adherence_partner_rel': None}

    def test_valid_form(self):
        """Test to verify whether  Treatment form will submit"""
        form = TreatmentForm(data=self.data)
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_if_perinatal_infection_pmtct(self):
        """Test when the disease is perinatal infection"""
        self.data['perinatal_infection'] = YES
        form = TreatmentForm(data=self.data)
        self.assertIn(
            'You selected perinatal infection',
            form.errors.get('perinatal_infection', []))

    def test_if_not_perinatal_infection_pmtct(self):
        """Test when the disease is not perinatal infection"""
        form = TreatmentForm(data=self.data)
        self.assertIn(
            'You have not selected perinatal infection',
            form.errors.get('perinatal_infection', []))

    def test_if_enrolled_in_pmtct_(self):
        """"Test to see if enrolled in pmtct"""
        self.data['pmtct'] = YES
        form = TreatmentForm(data=self.data)
        self.assertIn(
            'You have been enrolled in pmtct',
            form.errors.get('pmtct', []))

    def test_if_not_enrolled_in_pmtct(self):
        """Test when not enrolled in pmtct"""
        form = TreatmentForm(data=self.data)
        self.assertNotIn(
            'you are not enrolled in pmtct',
            form.errors.get('pmtct', []))

    def test_if_perinatal_infection_pmtct_rx_given(self):
        """Test to see if perinatal infection pmtct reason given"""
        self.data['pmtct_rx']
        form = TreatmentForm(data=self.data)
        self.assertIn(
            'you have given perinatal infection pmtct reason',
            form.errors.get('pmtct_rx', []))

    def test_if_perinatal_infection_pmtct_rx_not_given(self):
        """Test when perinatal infection pmtct reason is not given"""
        form = TreatmentForm(data=self.data)
        self.assertNotIn(
            'you have not given the perinatal infection pmtct reason',
            form.errors.get('pmtct_rx', []))
