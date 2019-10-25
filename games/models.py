from django.db import models

# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    nameoriginal = models.CharField(max_length=200, verbose_name='Оригинальное название')
    have = models.BooleanField(verbose_name='Наличие игры')
    min_player = models.IntegerField()
    max_player = models.IntegerField()
    disc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

