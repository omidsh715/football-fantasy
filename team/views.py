from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from players.models import Player
from .team import Team
from .models import TeamModel
from week.models import Week

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
    confirmed_team = team.confirm_team()
    week = Week.current_week.all()
    print(week)
    if not team:
        return redirect('team:draft')
    TeamModel.objects.create(week=week, user=request.user, team=confirmed_team) # noqa
    return redirect('players:list')
