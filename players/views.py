from django.shortcuts import render
from .models import Player
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
class PlayersListView(ListView):
    model = Player
    template_name = 'players/players_list.html'
    context_object_name = 'players'


@method_decorator(login_required, name='dispatch')
class PlayerDetailView(DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'players/player_detail.html'
