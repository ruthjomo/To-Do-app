from django import forms
# from .forms import *
from .models import *


class myTaskForm(forms.ModelForm):

    class Meta:
        model = myTask
        fields = '__all__'

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']




