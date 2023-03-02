from django.db import models
from datetime import date
from PIL import Image
from django.conf import settings
import os
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

def gen_path(filename, dirname):
    '''Формирует логику хранения постеров'''
    now = date.today()
    title_path = dirname.replace(':', '')
    save_path = r'photos/' + title_path + r'/%s/%s/%s' % (now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"))
    absolute_path_dir = settings.MEDIA_ROOT + r'/' + save_path
    absolute_path_file = absolute_path_dir + r'/' + filename
    if not os.path.exists(absolute_path_dir):
        os.makedirs(absolute_path_dir)
    return absolute_path_file


def sc_upload_to(instance, filename):
    '''Формирует логику хранения скриншотов'''
    now = date.today()
    part_path = instance.game.title.replace(':', '')
    return os.path.join('photos', part_path, 'screen',
                        r'%s/%s/%s' % (now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")), filename)


class Platforms(models.Model):
    '''Платформы'''
    title = models.CharField(max_length=100, verbose_name='Название платформы')
    description = models.TextField(verbose_name='Описание платформы')
    img = models.ImageField(blank=True, verbose_name='Фото платформы')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plat', kwargs={'plat_id': self.pk})

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class Category(models.Model):
    '''Жанры игр'''
    title = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')
    cat_slug = models.SlugField(verbose_name='url игры', unique=True, max_length=100)

    def get_absolute_url(self):
        return reverse('cat', kwargs={'slug': self.cat_slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Developers(models.Model):
    '''Разработчики игр'''
    title = models.CharField(max_length=100, verbose_name='Название компании')
    description = models.TextField(verbose_name='Описание компании')
    img = models.ImageField(blank=True, verbose_name='Логотип')
    dev_slug = models.SlugField(verbose_name='url игры', unique=True, max_length=100)

    def get_absolute_url(self):
        return reverse('dev', kwargs={'slug': self.dev_slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Разработчики'
        verbose_name_plural = 'Разработчики'


class Games(models.Model):
    '''В данном классе описаны основные поля Игр'''
    title = models.CharField(max_length=100, verbose_name='Название')
    slogan = models.CharField(max_length=100, verbose_name='Слоган', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    poster = models.ImageField(blank=True, verbose_name='Постер', upload_to=None, max_length=200)
    year = models.PositiveSmallIntegerField(verbose_name='Дата выхода', blank=True, null=True)
    realease_pc = models.DateField(verbose_name='Релиз на ПК', default=date.today)
    realease_console = models.DateField(verbose_name='Релиз на консолях', default=date.today)
    developers = models.ManyToManyField(Developers, verbose_name='Разработчики', related_name='game_dev')
    platforms = models.ManyToManyField(Platforms, verbose_name='Платформы', related_name='game_plat')
    category = models.ManyToManyField(Category, verbose_name='Категории', related_name='game_cat')
    trailer = models.URLField(verbose_name='Трейлер с ютуба', max_length=200, blank=True)
    is_pub = models.BooleanField(verbose_name='Опубликовать?', default=True, blank=True)
    game_slug = models.SlugField(verbose_name='url игры', unique=True, max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_game', kwargs={'slug': self.game_slug})

    def save(self, *args, **kwargs):
        if self.poster and not os.path.exists(self.poster.path):
            res_img = Image.open(self.poster).resize((300, 428))
            new_path = gen_path(self.poster.name, self.title)
            res_img.save(new_path)
            self.poster = new_path
        super(Games, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['realease_pc']


class GameScreen(models.Model):
    '''Скриншоты игр'''
    game = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE)
    screen = models.ImageField(blank=True, verbose_name='Скриншот', upload_to=sc_upload_to)

    def __str__(self):
        return self.game.title

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'


class SystemReq(models.Model):
    '''Системные требования для игры'''
    os = models.CharField(max_length=50, verbose_name='Операционная система', default='Windows 10')
    proc = models.CharField(max_length=50, verbose_name='Процессор', default='Pentium 3')
    oper_memory = models.SmallIntegerField(verbose_name='Оперативная память', help_text='Указывать в МБ', blank=True)
    phys_memory = models.SmallIntegerField(verbose_name='Свободная память на диске', help_text='Указывать в МБ',
                                           blank=True)
    videocard = models.CharField(max_length=50, verbose_name='Видеокарта', default='Pentium 3', blank=True)
    soundcard = models.CharField(max_length=50, verbose_name='Звуковая карта', default='Pentium 3', blank=True)
    game = models.OneToOneField(Games, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.game.title

    class Meta:
        verbose_name = 'Системные требования'
        verbose_name_plural = 'Системные требования'

class RaitingStar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезды рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']

class Raiting(models.Model):
    usrname = models.ForeignKey(User, verbose_name='Имя пользователя', on_delete=models.SET_NULL, null=True)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name='Звезды рейтинга')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name='Игра')


    def __str__(self):
        return f'{self.usrname} - {self.star} - {self.game}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
