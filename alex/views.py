
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from alex.models import  Contact
from Portofolio import settings
# Create your views here.
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'home/homepage.html'
    fields = '__all__'
    success_url = reverse_lazy('homepage')
