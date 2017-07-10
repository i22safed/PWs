from django.shortcuts import render
from .models import Equipo,Jugador

# Create your views here.

def team_list(request):
    return render(request, 'gestion/team_list.html',{})
