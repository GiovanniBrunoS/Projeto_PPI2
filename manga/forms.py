from django import forms

from .models import Manga, MangaChapter

class MangaForm(forms.ModelForm):

    class Meta:
        model = Manga
        fields = ('author', 'artist', 'title', 'description')

class ChapterForm(forms.ModelForm):

    class Meta:
        model = MangaChapter
        fields = ('chapter_number', 'title', 'language', 'chapter')