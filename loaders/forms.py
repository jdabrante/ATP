from django import forms


class LoadDataForm(forms.Form):
    match = forms.FileField()
    player = forms.FileField()
    stats = forms.FileField()
