from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField("Название игры", max_length=150)
    results = models.JSONField(blank=True, null=True)
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_for_user_1', blank=True, null=True)
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_for_user_2', blank=True, null=True)

    def __str__(self):
        return f'Игра {self.title}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        