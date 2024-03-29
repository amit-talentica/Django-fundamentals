from django.shortcuts import render
from gameplay.models import Game

# Create your views here.
def home(request):
    games_first_player = Game.objects.filter(
         first_player=request.user,
         status='F'
    )
    games_second_player = Game.objects.filter(
         second_player=request.user,
         status='S'
   )
    all_my_games = list(games_first_player) + \
                   list(games_second_player)

    return render(request, "player/home.html",
              {'games': all_my_games})