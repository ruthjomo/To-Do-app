from django import forms
# from .forms import *
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = '__all__'

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']




