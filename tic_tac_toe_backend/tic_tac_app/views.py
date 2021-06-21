from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import GameSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Game
from rest_framework.permissions import *

class GameListViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
    
def index(request):
    return HttpResponse('фыво')
