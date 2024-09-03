from django.urls import path
from .views import GamesListView, GameDetail

urlpatterns = [
    path('game_list/',GamesListView.as_view(), name='game_list'),
    path('game_detail/<int:pk>/',GameDetail.as_view(),name='game_detail'),
]