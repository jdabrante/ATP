from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from players.models import Player
from matches.models import Matches
from .forms import LoadDataForm
from .utils import read_csv
import redis
from django.conf import settings

# Connect to redis
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB) 


def load_data(request):
    if request.method == "POST":

        form = LoadDataForm(request.POST, request.FILES)
        if form.is_valid():
            for player in read_csv(request.FILES['player']):
                birthdate = datetime.strptime(player['birthdate'], "%Y-%m-%d")
                Player.objects.create(name=player['name'], hand=player['hand'], country=player['country'], birthdate=birthdate)
                r.set([player['player_id']], Player.objects.latest('id').id)

            for match in read_csv(request.FILES['match']):
                date = datetime.strptime(match['date'], "%Y-%m-%d")
                Matches.objects.create(tournament=match['tournament'], date=date, match_round=match['round'], duration=match['duration'])
                r.set([match['match_id']], Matches.objects.latest('id').id)
            
            for stat in read_csv(request.FILES['stats']):
                db_match_id = r.get([stat['match_id']])
                db_player_id = r.get([stat['player_id']])
                match = get_object_or_404(Matches, id=db_match_id)
                player = get_object_or_404(Player, id=db_player_id)
                if stat['winner'] == 'TRUE':
                    match.winner = player
                else: 
                    match.loser = player
                match.save()
            return HttpResponse('Upload success')
        return HttpResponse('Error')
    else:
        form = LoadDataForm()
    return render(request, 'loaders/loaddata.html', dict(form=form))
