from .models import Report
from django import forms

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['Topic','User','Computer_Equipment','Department','Details','Status']
        widgets = {
            'Topic' : forms.TextInput(attrs={"class":"form-control"}),
            'Computer_Equipment' : forms.TextInput(attrs={"class":"form-control"}),
            'User' : forms.TextInput(attrs={"class":"form-control"}),
            'Department' : forms.TextInput(attrs={"class":"form-control"}),
            'Details' : forms.Textarea(attrs={"class":"form-control"}),
            'Status' : forms.Select(attrs={"class":"form-control"}),
        }