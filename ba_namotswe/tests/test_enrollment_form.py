from datetime import date, datetime
from django.test import TestCase

from dateutil.relativedelta import relativedelta

from edc_constants.constants import YES, MALE
from ba_namotswe.forms.enrollment_form import EnrollmentForm
#from ba_namotswe.models.Enrollment import Subject_identifier
from ba_namotswe.tests.factories.registered_subject_factory import RegisteredSubjectFactory


class TestEnrollment(TestCase):

    def setUp(self):
        self.registered_subject = RegisteredSubjectFactory()

        self.data = {
            'registered_subject': self.registered_subject.id,
            'initials': 'KK',
            'subject_identifier': '06609090-2',
            'dob': date(1988, 7, 7),
            'gender': MALE,
            'report_datetime': datetime.now(),
            'is_eligible': True,
            'initial_visit_date': date.today() - relativedelta(years=3),
            'caregiver_relation': 'mother',
            'caregiver_relation_other': None,
            'weight_measured': YES,
            'weight': 120,
            'height_measured': YES,
            'height': 120,
            'hiv_diagnosis_date': date.today(),
            'art_initiation_date': date.today()}

    def test_valid_form(self):
        """Test to verify that enrollment form will submit"""
        form = EnrollmentForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_date_of_birth_provided(self):
        """Test to see if valid date_of_birth is provided"""
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided valid dob',
            form.errors.get('date_of_birth', []))

    def test_date_of_birth_provided_not_valid(self):
        """Test to see if valid date_of_birth is provided"""
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided invalid dob, please correct',
            form.errors.get('date_of_birth', []))

    def test_right_gender_provided(self):
        """Test to see if correct gender is provided"""
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided correct sex, please correct',
            form.errors.get('gender', []))

    def test_gender_is_provided(self):
        """Test to see if gender is provided"""
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided sex',
            form.errors.get('gender', []))

    def test_caretaker_relation(self):
        """Test to see who the caretaker is """
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided the caretaker as other',
            form.errors.get('caregiver_relation_other', []))

    def test_caretaker_relation_is(self):
        """Test to see who the caretaker is """
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided the caretaker as other',
            form.errors.get('caregiver_relation_other', []))

    def test_if_weight_provided(self):
        """Test to see if weight is given """
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided the weight',
            form.errors.get('weight', []))

    def test_if_height_provided(self):
        """Test to see if height is given """
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'You provided the height',
            form.errors.get('height', []))

    def test_if_anti_retroviral_treatment_given(self):
        """Test to see if ART is given """
        form = EnrollmentForm(data=self.data)
        self.assertNotIn(
            'ART provided',
            form.errors.get('height', []))
