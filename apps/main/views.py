from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'

class BrowseView(TemplateView):
    template_name = 'pages/browse.html'

class DetailView(TemplateView):
    template_name = 'pages/details.html'

class StreamsView(TemplateView):
    template_name = 'pages/streams.html'

class ProfileView(TemplateView):
    template_name = 'pages/profile.html'
