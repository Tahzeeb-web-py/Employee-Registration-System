from django import forms
from .models import Employee

class emp_forms(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
        labels={
            'mobileno':'Mobile No'
        }
    def __init__(self, *args, **kwargs):
        super(emp_forms, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label= 'Select'