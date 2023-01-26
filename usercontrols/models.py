from django.db import models
from django.contrib.auth.models import User
from games.models import *

# Create your models here.

class Comments(models.Model):
    name = models.ForeignKey(User, verbose_name='Имя пользователя', on_delete=models.SET_NULL, null=True)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='', on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} - {self.game}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'