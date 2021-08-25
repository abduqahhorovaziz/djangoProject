from django.shortcuts import render
from django.views.generic import TemplateView





# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PortPageView(TemplateView):
    template_name = 'portfolio.html'

class ContPageView(TemplateView):
    template_name = 'contact.html'