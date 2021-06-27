from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CustomUser as User

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'birthday')
        widgets = {
            'birthday': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save user'))