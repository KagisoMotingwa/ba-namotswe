from django.contrib import admin

from edc_base.modeladmin.mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin)
from edc_visit_tracking.admin import VisitAdminMixin

from .forms import (
    SubjectConsentForm, SubjectVisitForm, TBHistoryForm, TreatmentForm, EnrollmentForm, ExtractionForm,
    AdherenceCounsellingForm, ArvHistoryForm, AssessmentHistoryForm, DeathForm, PregnancyHistoryForm,
    TransferHistoryForm, OiForm, ArtRegimenForm, ExtractionChecklistForm)
from .models import (
    SubjectConsent, SubjectVisit, ExtractionChecklist, Enrollment, Oi, Extraction, Treatment, ArtRegimen,
    Appointment, TbHistory, AdherenceCounselling, ArvHistory, AssessmentHistory, Death, PregnancyHistory,
    TransferHistory)
from ba_namotswe.models.arv import Arv
from ba_namotswe.models.pregnancy import Pregnancy
from ba_namotswe.models.transfer import Transfer
from ba_namotswe.admin_site import ba_namotswe_admin
from django.contrib.admin.templatetags.admin_list import date_hierarchy


class BaseModelAdmin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                     ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin, admin.ModelAdmin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        return request.GET.get('next')


class BaseCrfModelAdmin(BaseModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subject_visit' and request.GET.get('subject_visit'):
            kwargs["queryset"] = SubjectVisit.objects.filter(pk=request.GET.get('subject_visit', 0))
        return super(BaseCrfModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ExtractionChecklist, site=ba_namotswe_admin)
class ExtractionChecklistAdmin(BaseCrfModelAdmin):
    form = ExtractionChecklistForm
    list_filter = ('subject_visit', 'arv_changes', 'tb_diagnosis', )
    radio_fields = {
        'arv_changes': admin.VERTICAL,
        'tb_diagnosis': admin.VERTICAL,
        'oi_diagnosis': admin.VERTICAL,
        'preg_diagnosis': admin.VERTICAL,
        'counselling_adhere': admin.VERTICAL,
        'treatment': admin.VERTICAL,
        'transfer': admin.VERTICAL,
        'death': admin.VERTICAL}


@admin.register(Enrollment, site=ba_namotswe_admin)
class EnrollmentAdmin(BaseModelAdmin):
    form = EnrollmentForm
    radio_fields = {
        'caregiver_relation': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'weight_measured': admin.VERTICAL,
        'height_measured': admin.VERTICAL}

    list_display = ('dashboard', 'initial_visit_date', 'hiv_diagnosis_date', 'art_initiation_date', )


@admin.register(Appointment, site=ba_namotswe_admin)
class AppointmentAdmin(BaseModelAdmin):
    list_filter = ('best_appt_datetime', )


@admin.register(SubjectVisit, site=ba_namotswe_admin)
class SubjectVisitAdmin(VisitAdminMixin, BaseModelAdmin):

    form = SubjectVisitForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'appointment' and request.GET.get('appointment'):
            kwargs["queryset"] = Appointment.objects.filter(pk=request.GET.get('appointment', 0))
        return super(VisitAdminMixin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Extraction, site=ba_namotswe_admin)
class ExtractionAdmin(BaseCrfModelAdmin):
    list_filter = ('subject_visit', )
    form = ExtractionForm
    # fields = ()
    readonly_fields = ('subject_visit', )
    filter_horizontal = ('art_history', 'oi_history')
    radio_fields = {
        'height_measured': admin.VERTICAL,
        'weight_measured': admin.VERTICAL,
        'hospitalized': admin.VERTICAL,
        'tb': admin.VERTICAL,
        'tb_type': admin.VERTICAL,
        'tb_method': admin.VERTICAL,
        'io': admin.VERTICAL,
        'ctx': admin.VERTICAL,
        'ctx_table': admin.VERTICAL,
        'pregnant_and_rx': admin.VERTICAL,
        'hiv_status_aware': admin.VERTICAL,
        'hiv_disclosed_others': admin.VERTICAL,
        'hiv_caregiver_disclosed_others': admin.VERTICAL,
        'transferred': admin.VERTICAL,
        'transferred_to': admin.VERTICAL,
        'deceased': admin.VERTICAL,
    }


class PregnancyInline(admin.TabularInline):
    model = Pregnancy


@admin.register(PregnancyHistory, site=ba_namotswe_admin)
class PregnancyHistoryAdmi(BaseCrfModelAdmin):
    inlines = [PregnancyInline]
    form = PregnancyHistoryForm


class TransferInline(admin.TabularInline):
    model = Transfer


@admin.register(TransferHistory, site=ba_namotswe_admin)
class TransferHistoryAdmin(BaseCrfModelAdmin):
    inlines = [TransferInline]
    radio_fields = {
        'transfer_loc': admin.VERTICAL}
    form = TransferHistoryForm


@admin.register(Death, site=ba_namotswe_admin)
class DeathAdmin(BaseCrfModelAdmin):
    list_filter = ('subject_visit', )
    form = DeathForm


@admin.register(AssessmentHistory, site=ba_namotswe_admin)
class AssessmentHistoryAdmin(BaseCrfModelAdmin):
    list_filter = ('subject_visit', )
    form = AssessmentHistoryForm


class ArvInline(admin.TabularInline):
    model = Arv


@admin.register(ArvHistory, site=ba_namotswe_admin)
class ArvHistoryAdmin(BaseCrfModelAdmin):
    inlines = [ArvInline]
    form = ArvHistoryForm


@admin.register(AdherenceCounselling, site=ba_namotswe_admin)
class AdherenceCounsellingAdmin(BaseCrfModelAdmin):
    list_filter = ('adherence_partner', )
    radio_fields = {
        'adherence_partner': admin.VERTICAL}
    form = AdherenceCounsellingForm


@admin.register(Treatment, site=ba_namotswe_admin)
class TreatmentAdmin(BaseCrfModelAdmin):
    list_filter = ('perinatal_infection', )
    form = TreatmentForm


@admin.register(Oi, site=ba_namotswe_admin)
class OiAdmin(BaseCrfModelAdmin):
    list_filter = ('oi_type', )
    radio_fields = {
        'oi_type': admin.VERTICAL}
    form = OiForm


@admin.register(ArtRegimen, site=ba_namotswe_admin)
class ARTRegimenAdmin(BaseCrfModelAdmin):
    list_filter = ('name', )
    form = ArtRegimenForm


@admin.register(TbHistory, site=ba_namotswe_admin)
class TBHistoryAdmin(BaseCrfModelAdmin):
    form = TBHistoryForm
    radio_fields = {
        'tb_type': admin.VERTICAL,
        'tb_test': admin.VERTICAL}


@admin.register(SubjectConsent, site=ba_namotswe_admin)
class SubjectConsentAdmin(BaseModelAdmin):

    dashboard_type = 'subject'
    form = SubjectConsentForm
