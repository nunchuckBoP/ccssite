from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML
from timetrack.models import Timesheet
from crispy_bootstrap5.bootstrap5 import FloatingField

class TimesheetForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TimesheetForm, self).__init__(*args, **kwargs)

        # if you pass a FormHelper constructior a form instance
        # It builds a default layout with all of its fields
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            FloatingField('start_date'),
            FloatingField('end_date'),
            Submit('Submit', 'Submit'),
            HTML('<a class="btn btn-primary" href="/timetrack/sheet/list">Cancel</a>')
        )

    class Meta:
        model = Timesheet
        fields = ['start_date', 'end_date']