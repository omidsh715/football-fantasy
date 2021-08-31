from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from players.models import Player
from .team import Team
from .models import TeamModel
from week.models import Week
from django.views.generic.list import ListView
from django.contrib import messages
# Create your views here.


@require_POST
def add_player(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.add(player)
    return redirect('team:draft')


@require_POST
def remove_player(request, player_id):
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.remove(player)
    return redirect('team:draft')


@require_POST
def clear_draft(request):
    team = Team(request)
    team.clear()
    return redirect('team:draft')


def draft_team(request):
    team = Team(request)
    return render(request, 'team/draft_team.html', {'team': team})


@require_POST
def confirm(request):
    team = Team(request)
    week = Week.current_week.all()
    confirmed_team = team.confirm_team()
    if not confirmed_team:
        messages.error(request, "can't save your draft team")
        return redirect('team:draft')
    TeamModel.objects.update_or_create(week=week, user=request.user, team=confirmed_team) # noqa
    messages.success(request, "your team is saved")
    return redirect('team:main')


class TeamsList(ListView):
    template_name = 'team/list_of_teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return TeamModel.objects.filter(user=self.request.user,)


def show_team(request, week=Week.current_week.all()):
    team = get_object_or_404(TeamModel, user=request.user, week=week)
    player_ids = team.team.keys()
    players = Player.objects.filter(id__in=player_ids) # noqa
    return render(request, 'team/team.html', {'players': players})


