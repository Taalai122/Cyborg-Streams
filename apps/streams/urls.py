from django.urls import path
from . import views

app_name = 'streams'

urlpatterns = [
    path('start_stream/', views.StartStreamView.as_view(), name='start_stream'),
    path('live_stream/<int:stream_id>/', views.LiveStreamView.as_view(), name='live_stream'),
    path('end_stream/<int:stream_id>/', views.EndStreamView.as_view(), name='live_stream')
    # path('streams/', StreamListView.as_view(), name='streams'),
]
