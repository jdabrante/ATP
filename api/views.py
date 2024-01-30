from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from matches.models import Matches
from players.models import Player

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
