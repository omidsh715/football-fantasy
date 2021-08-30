from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from players.models import Player
from .team import Team


# Create your views here.

@require_POST
def add_player(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.add(player)
    return redirect('team:draft')


def remove_player(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.remove(player)
    return redirect('team:draft')


def clear_draft(request):
    team = Team(request)
    team.clear()
    return redirect('team:draft')


def draft_team(request):
    team = Team(request)
    print(request.session)
    return render(request, 'team/draft_team.html', {'team': team})


def confirm(request):
    team = Team(request)
    is_valid = team.confirm_team()
    if is_valid:
        return redirect('players:list')
    return redirect('team:draft')
