from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('browse/', BrowseView.as_view(), name='browse'),
    path('details/', DetailView.as_view(), name='details'),
    path('streams/', StreamsView.as_view(), name='streams'),
    path('profile/', ProfileView.as_view(), name='profile'),
]