from rest_framework import serializers
from players.models import Player
from matches.models import Matches




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'hand', 'country', 'birthdate']

class MatchesSerializer(serializers.ModelSerializer):
    winner, loser = PlayerSerializer(), PlayerSerializer()
    class Meta:
        model = Matches
        fields = ['tournament', 'date', 'match_round', 'duration', 'winner', 'loser']

