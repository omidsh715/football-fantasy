from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from players.models import Player
from .team import Team
from .models import TeamModel
from week.models import Week
from django.views.generic.list import ListView
from django.contrib import messages
from points.models import PlayerPoint
# Create your views here.


@require_POST
def add_player(request, player_id):
    """

    receives player id and add it to team session

    """
    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.add(player)
    return redirect('team:draft')


@require_POST
def remove_player(request, player_id):
    """

    receives player id and remove it from team session

    """

    team = Team(request)
    player = get_object_or_404(Player, id=player_id)
    team.remove(player)
    return redirect('team:draft')


@require_POST
def clear_draft(request):
    """

    clear team session

    """

    team = Team(request)
    team.clear()
    return redirect('team:draft')


def draft_team(request):
    team = Team(request)
    return render(request, 'team/draft_team.html', {'team': team})


@require_POST
def confirm(request):
    """

    validate team session and if it's valid saves it to TeamModel
    if it's not valid show an error massage

    """
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
    """
    show list teams that user created within weeks
    """
    template_name = 'team/list_of_teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return TeamModel.objects.filter(user=self.request.user,)


def show_team(request, week=Week.current_week.all()):
    """

    show user's team of given week
    default week is current week

    """
    team = get_object_or_404(TeamModel, user=request.user, week=week)

    player_ids = team.team.keys()
    players = Player.objects.filter(id__in=player_ids) # noqa
    points = PlayerPoint.objects.filter(week=week, player__in=players)
    total_points = sum([item.point for item in points])
    return render(request, 'team/team.html', {'players': players, 'points':points, 'total_points': total_points})


