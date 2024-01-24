from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from matches.models import Matches
from players.models import Player

from .forms import MatchAI
from .serializers import MatchesSerializer, PlayerSerializer


class PlayerListView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class MatchListView(generics.ListAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer


class MatchesWinnerView(APIView):
    queryset = Matches.objects.all()

    def get(self, request, pk, format=None):
        match = get_object_or_404(Matches, pk=pk)
        return Response(PlayerSerializer(match.winner).data)


class MatchesLoserView(APIView):
    queryset = Matches.objects.all()

    def get(self, request, pk, format=None):
        match = get_object_or_404(Matches, pk=pk)
        return Response(PlayerSerializer(match.loser).data)


@csrf_exempt
def create_lore(request):
    if request.method == 'POST':
        form = MatchAI(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tournament = cd['matches'].tournament
            winner = cd['matches'].winner.name
            loser = cd['matches'].loser.name
            message = (
                f'What happened in the tournament {tournament} where {winner} and {loser} played'
            )
    else:
        form = MatchAI()
