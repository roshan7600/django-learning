from django import forms

def Check_for_a(value):
    if value[0].lower() == 'a':
        raise forms.ValidationError('Name cannot start with "a"')

class StudentForm(forms.Form):
    Sname = forms.CharField(validators=[Check_for_a])
    Sage = forms.IntegerField()
    Semail = forms.EmailField()
    