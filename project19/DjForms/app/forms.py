from django import forms


g=[('MALE','male'),('FEMALE','female')]
c=[('PYTHON','python'),('DJANGO','django'),('SQL','sql')]
class StudentDjForm(forms.Form):
    stname=forms.CharField()
    stage=forms.IntegerField()
    # gender=forms.CharField(choices=g)
    # gender=forms.CharField(choices=g,widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=g, widget=forms.RadioSelect)
    # cources=forms.MultipleChoiceField(choices=c)
    cources=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea)



