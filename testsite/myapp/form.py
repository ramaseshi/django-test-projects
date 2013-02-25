from django import forms

class SumbitForm(forms.Form):
    text = forms.CharField(max_length=255)
