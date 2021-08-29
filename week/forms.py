from django  import forms


WEEK_NUMBER_CHOICES = [(i, str(i)) for i in range(1, 39)]


class WeekNumberForm(forms.Form):
    week_number = forms.ChoiceField(choices=WEEK_NUMBER_CHOICES)
