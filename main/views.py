from django.shortcuts import render
from .models import Leader_Board, Player 
from .forms import playerform
from django.http import HttpResponseRedirect
from random import choice
from string import digits

# Create your views here.
def home(response):
    return render(response, "main/base.html")


def menu(request):
    # Variables
    submitted = False
    leaderboard = Leader_Board.objects.get(id=2)
    player = Player.objects.all()
    
    # Inserting username into database(Player)
    if request.method == "POST": 
        form = playerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("menu/game_on/")
    else:
        form = playerform
        if "submitted" in request.GET:
            submitted = True 

    context = {
        'form':form,
        'submitted': submitted,
        'LEADERBOARD': leaderboard,
        'player': player
    }

    return render(request, "main/menu.html", context=context)


def game_on(request):    
    answers = request.POST.get("answer_user")      
    random_number = choice(digits) 
    guess = Player.objects.first()
    number = getattr(guess, "guesses")

    return render(request, "main/game_on.html", {"answers": answers, "random_number": random_number, "number": number})
        
    

        

  
    