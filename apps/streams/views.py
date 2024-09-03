from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View

from ..games.models import Games

class StartStreamView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'pages/start_stream.html')

    def post(self, request):
        stream =  Stream.objects.create(streamer=request.user,
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            game = Games.objects.get(id=request.POST.get('game')),
            live = True,
            )
        return redirect('pages/live_stream',stream.id)#'streams:stream', stream.id

class LiveStreamView(LoginRequiredMixin,View):
    def get(self, request, stream_id):
        stream = Stream.objects.get(id=stream_id,streamer=request.user,
            live=True)
        return render(request, 'pages/live_stream.html',
                      {'stream': stream})

class EndStreamView(LoginRequiredMixin, View):
    def get(self, request, stream_id):
        stream = Stream.objects.get(id=stream_id, streamer=request.user,live=True)
        stream.live = False
        stream.save()
        return redirect('streams:index', stream.id)


# class StreamListView(ListView):
#     model = Stream
#     template_name = 'pages/streams.html'
#     context_object_name = 'streams'
#     queryset = Stream.objects.all()
