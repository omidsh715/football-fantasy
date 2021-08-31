from django.forms import forms
from week.models import Week


class SelectWeekForm(forms.Form):
    
    class Meta:
        model = Week
        fields = ('week',)
