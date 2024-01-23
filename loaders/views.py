from datetime import datetime

from django.shortcuts import render

from players.models import Player

from .forms import LoadDataForm
from .utils import read_csv

# def load_data(request):
#     if request.method == 'POST':
#         form = LoadDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             messages.add_message(request, messages.INFO, 'Hi')
#             return render(request, 'loaders/success.html')
#     else:
#         form = LoadDataForm()
#     return render(request, 'loaders/loaddata.html', dict(form=form))


def load_data(request):
    if request.method == "POST":
        players_id = {}
        matches_id = {}
        form = LoadDataForm(request.POST, request.FILES)
        if form.is_valid():
            for player in read_csv(request.FILES['player']):
                birthdate = datetime.strptime(player['birthdate'], "%Y-%m-%d")
                Player.objects.create(
                    name=player['name'],
                    hand=player['hand'],
                    country=player['country'],
                    birthdate=birthdate,
                )
                players_id[Player.objects.lastest('id')] = player['player_id']
            for match in read_csv(request.FILES['match'], '')
    else:
        form = LoadDataForm()
    return render(request, 'loaders/loaddata.html', dict(form=form))
