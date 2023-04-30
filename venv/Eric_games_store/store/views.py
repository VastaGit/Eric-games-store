from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Game

# def store(request):
#   template = loader.get_template('first.html')
#   return HttpResponse(template.render())

def store(request):
  mygames = Game.objects.all().values()
  template = loader.get_template('all_games.html')
  context = {
    'mygames': mygames,
  }
  return HttpResponse(template.render(context, request))