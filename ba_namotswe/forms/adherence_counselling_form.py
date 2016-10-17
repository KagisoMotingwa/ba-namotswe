from django import forms

from ba_namotswe.models.adherence_counselling import Adherence_Counselling
from edc_base.utils.age import age
from edc_constants.constants import NO, YES
from datetime import date


class AdherencePartnerRelationForm(forms.ModelForm):

    def clean(self):
        self.validate_adherence_partner_relation_other()
        return self.cleaned_data

    def validate_adherence_partner_relation_other(self):
        if self.cleaned_data.get('adherence_partner_relation') != 'OTHER':
            if self.cleaned_data.get('adherence_partner_relation_other'):
                raise forms.ValidationError({
                    'adherence_partne_relation_other': [
                        'You should not enter other adherence_partner relation as you have already entered a adherence_partner relation']})
        else:
            if not self.cleaned_data.get('adherence_partner_relation_other'):
                raise forms.ValidationError({
                    'adherence_partner_relation_other': [
                        'You should enter other adherence_partner relation as you have selected OTHER adherence_partner relation']})
        return self.cleaned_data

    class Meta:
        model = Adherence_Counselling
        fields = '__all__'
