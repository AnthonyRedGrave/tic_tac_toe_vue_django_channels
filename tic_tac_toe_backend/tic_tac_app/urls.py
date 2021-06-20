from django.urls import path
from .views import GameListViewSet

urlpatterns = [
    path('game/list/', GameListViewSet, name="game_list")
]