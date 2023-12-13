from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from jobs.models import Job
from crispy_bootstrap5.bootstrap5 import FloatingField

class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        # if you pass a FormHelper constructior a form instance
        # It builds a default layout with all of its fields
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            FloatingField('number_string'),
            FloatingField('title'),
            Submit('Submit', 'Submit')
        )

    class Meta:
        model = Job
        fields = ['number_string', 'title']