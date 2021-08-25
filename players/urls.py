from django.urls import path
from .views import PlayersListView, PlayerDetailView
from django.contrib.auth.decorators import login_required
app_name = 'players'

urlpatterns = [
    path('', PlayersListView.as_view(), name='list'),
    path('<int:pk>/', login_required(PlayerDetailView.as_view()), name='detail'),
]
