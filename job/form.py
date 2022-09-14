from django import forms
from .models import Job_Aplication , Job


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Job_Aplication
        fields = ['name','email','website','cv','cover_letter']

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug',)