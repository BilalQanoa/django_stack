from django import forms
from .models import Review

class TestForm (forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            'first_name' : 'Enter First Name: ',
            'last_name' : 'Enter Last Name: ',
            'age' : 'Enter Age: ',
        }

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

        error_messages = {
            'age' : {
                'min_value' : 'min value is 18',
                'max_value' : 'max value is 32'
            }
        }