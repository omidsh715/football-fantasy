from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [

    path('', views.draft_team, name='draft'),
    path('add/<int:player_id>/', views.add_player, name='add'),
    path('remove/<int:player_id>/', views.remove_player, name='remove'),
    path('clear/', views.clear_draft, name='clear'),
    path('confirm/', views.confirm, name='confirm'),

]
