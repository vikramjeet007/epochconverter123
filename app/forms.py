from django import forms

class EpochForm(forms.Form):
    epochtime = forms.IntegerField(required=True)