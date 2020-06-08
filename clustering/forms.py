from django import forms
from django.core.exceptions import ValidationError

from .models import *


class FileForm(forms.Form):
    file = forms.FileField(label='file', required=True)


class AlgorithmForm(forms.Form):
    k = forms.IntegerField(label='k', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(1)],
                           required=True,
                           )
    eps = forms.FloatField(label='eps', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                           validators=[MinValueValidator(0)],
                           required=True,
                           )
    algorithm = forms.ChoiceField(label='algorithm', choices=[('k_mxt_w', 'k-MXT-W'), ('k_mxt', 'k-MXT')],
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  required=True,
                                  )

    def __init__(self, choices, *args, **kwargs):
        self.choices = choices
        super().__init__(*args, **kwargs)
        self.fields['latitude'] = forms.ChoiceField(label='latitude', choices=self.choices,
                                                    widget=forms.Select(attrs={'class': 'form-control'}),
                                                    )
        self.fields['longitude'] = forms.ChoiceField(label='longitude', choices=self.choices,
                                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                                     )
        self.fields['features'] = forms.MultipleChoiceField(label='features', choices=self.choices,
                                                            widget=forms.CheckboxSelectMultiple(
                                                                attrs={'class': 'form-check-input'}),
                                                            )
