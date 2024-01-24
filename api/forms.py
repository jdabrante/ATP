from django import forms

from matches.models import Matches


class MatchAI(forms.Form):
    matches = forms.ChoiceField(choices=Matches.objects.all())
