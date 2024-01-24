from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('players/', views.PlayerListView.as_view(), name='api_player_list'),
    path('players/<pk>/', views.PlayerDetailView.as_view(), name='api_player_detail'),
    path('matches/', views.MatchListView.as_view(), name='api_match_list'),
    path('matches/<pk>/', views.MatchDetailView.as_view(), name='api_match_detail'),
    path('matches/<pk>/winner/', views.MatchesWinnerView.as_view(), name='api_match_winner_detail'),
    path('matches/<pk>/loser/', views.MatchesLoserView.as_view(), name='api_match_loser_detail'),

]
