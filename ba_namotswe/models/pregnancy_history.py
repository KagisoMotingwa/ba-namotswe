from django import forms


class PregnancyHistory(forms.ModelForm):

    class Meta:
        app_label = 'ba_namotswe'

    pregnancy_details = models.CharField(
        max_length=7,
        verbose_name='Has the participant moved out of the household where last seen',
        choices=
            ('date_of_first_clinical_documentation_of_pregnancy', 'Date of First Clinical Documentation of Pregnancy'),
            ('date_of_delivery', 'Date of Delivery'),
        null=True,
        blank=False