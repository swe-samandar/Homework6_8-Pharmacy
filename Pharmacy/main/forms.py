from django import forms
from .models import Medication
from datetime import date
from django.utils import timezone

class MedsForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'


