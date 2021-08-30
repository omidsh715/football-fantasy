from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [

    path('', views.draft_team, name='draft'),
    path('add/<int:player_id>/', views.team_add, name='add'),
    path('remove/<int:player_id>/', views.team_remove, name='remove'),

]
