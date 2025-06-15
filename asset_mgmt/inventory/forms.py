from django import forms
from .models import NV, TS, BG

class NVForm(forms.ModelForm):
    class Meta:
        model = NV
        fields = '__all__'

class TSForm(forms.ModelForm):
    class Meta:
        model = TS
        fields = '__all__'

class BGForm(forms.ModelForm):
    class Meta:
        model = BG
        fields = '__all__'
        widgets = {'ngay_giao': forms.DateInput(attrs={'type':'date'})}