from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Group, Event
from django.urls import reverse_lazy

class DateInput(forms.DateInput):
    input_type = 'date'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'description']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['first_name', 'last_name', 'username', 'is_active']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'image_url']
        widgets = {
            'date': DateInput()
        }


