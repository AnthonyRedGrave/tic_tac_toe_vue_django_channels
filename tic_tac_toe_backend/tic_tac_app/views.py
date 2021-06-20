from django.shortcuts import render
from .serializers import GameSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Game

class GameListViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    
