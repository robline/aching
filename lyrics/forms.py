from django import forms

from .models import Verse

class AchingForm(forms.Form):

    question = forms.CharField(label='Your question:', max_length=512)
