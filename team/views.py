from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from players.models import Player
from .team import Team


# Create your views here.

@require_POST
def team_add(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.add(player)
    return redirect('team:detail')


def team_remove(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.remove(player)
    return redirect('team:detail')


def draft_team(request):
    team = Team(request)
    print(request.session)
    return render(request, 'team/draft_team.html', {'team': team})
