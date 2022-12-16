from django import forms
from .models import category, book


class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
