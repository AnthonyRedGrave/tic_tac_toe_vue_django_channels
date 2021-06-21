from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    user_name_1 = serializers.CharField(source='user_1')
    user_name_2 = serializers.CharField(source='user_2', required=False)

    class Meta:
        model = Game
        fields = ['id', 'title', 'results', 'user_name_1', 'user_name_2']

    def create(self, data):
        user = User.objects.get(username = data['user_1'])
        new_game = Game.objects.create(user_1 = user, title = data['title'])
        return new_game