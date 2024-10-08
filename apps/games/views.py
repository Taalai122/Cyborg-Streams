from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


class GamesListView(ListView):
    model = Games
    template_name = 'pages/game_list.html'
    context_object_name = 'games'
    queryset = Games.objects.all().order_by('-created_at')

class GameDetail(DetailView):
    model = Games
    template_name = 'pages/game_detail.html'
    context_object_name = 'game'
    queryset = Games.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['top_down'] = Games.object.order_by('-downloaded_count')[:5]
    #     return context