from .consumers import TicTacToeConsumer
from django.urls import re_path, path

ws_urlpatterns = [
    re_path(r'ws/game/(?P<game_id>\d+)/$', TicTacToeConsumer.as_asgi())
]