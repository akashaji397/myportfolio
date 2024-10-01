from django import forms

class AboutForm(forms.Form):
    short_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), required=True)
    image = forms.ImageField(required=True)


from django import forms

class EducationForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    year = forms.IntegerField(min_value=1900, max_value=2100, required=True)
    course = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

from django import forms
from .models import RecentWork

class RecentWorkForm(forms.ModelForm):
    class Meta:
        model = RecentWork
        fields = ['project_title', 'project_image', 'project_description']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 4}),
        }
