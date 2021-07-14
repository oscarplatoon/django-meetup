from django.shortcuts import render
from meetup_app.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
