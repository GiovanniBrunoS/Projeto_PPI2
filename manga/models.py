from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .validators import validate_file_extension, validate_image_extension


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manga(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class MangaChapter(models.Model):
    ENGLISH = 'EN'
    PORTUGUESE = 'PT'
    PORTUGUESE_PT = 'PT-pt'
    SPANISH = 'ES'
    LANGUAGES = [
        ('EN', 'en-us'),
        ('PT', 'pt-br'),
        ('PT-pt', 'pt-pt'),
        ('ES', 'es-es')
    ]
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    chapter_number = models.DecimalField(max_digits=6 ,decimal_places=1)
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=5, choices=LANGUAGES)
    created_date = models.DateTimeField(auto_now=True)
    chapter = models.FileField(blank=False, validators=[validate_file_extension])

    def __str__(self):
        return '{} - {} {}'.format(self.manga.title, self.chapter_number, self.title)

class MangaPage(models.Model):
    manga_chapter = models.ForeignKey(MangaChapter, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    page = models.ImageField(validators=[validate_image_extension])

    def __str__(self):
        return '{} - page {}'.format(self.manga_chapter.title, self.page_number)
