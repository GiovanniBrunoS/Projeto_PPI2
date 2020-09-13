from django.shortcuts import render, get_object_or_404, redirect
from zipfile import ZipFile
from PIL import Image
import base64

from .models import Manga, MangaChapter, MangaPage
from .forms import MangaForm, ChapterForm

# Create your views here.
def manga_list(request):
    manga_list = Manga.objects.order_by('title')
    return render(request, 'manga/manga_list.html', {'manga_list': manga_list})


def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    chapters = MangaChapter.objects.filter(manga=manga)
        
    return render(request, 'manga/manga_detail.html', {'manga': manga, 'chapters':chapters})


def manga_new(request):
     if request.method == "POST":
         form = MangaForm(request.POST)
         if form.is_valid():
             manga = form.save(commit=False)
             manga.save()
             return redirect('manga_detail', pk=manga.pk)
     else:
         form = MangaForm()
     return render(request, 'manga/manga_edit.html', {'form': form})


def manga_edit(request, pk):
     manga = get_object_or_404(Manga, pk=pk)
     if request.method == "POST":
         form = MangaForm(request.POST, instance=manga)
         if form.is_valid():
             manga = form.save(commit=False)
             manga.save()
             return redirect('manga_detail', pk=manga.pk)
     else:
         form = MangaForm(instance=manga)
     return render(request, 'manga/manga_edit.html', {'form': form})


def manga_remove(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    manga.delete()
    return redirect('manga_list')


def chapter_new(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    if request.method == "POST":
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.manga = manga
            chapter.save()
            return redirect('manga_detail', pk=manga.pk)
    else:
        form = ChapterForm()
    return render(request, 'manga/chapter_new.html', {'form': form})
        
'''            
            counter = 1
            with ZipFile(chapter.chapter, 'r') as zip:
                for entry in zip.namelist():
                    with zip.open(entry) as file:
                        img = Image.open(file)
                        img.save(img.filename)
                        page = MangaPage(manga_chapter=chapter, page_number=counter, page=img)
                        counter+=1
                        print('a')
                        page.save()
'''
    


def reader(request, mangapk, chapterpk):
    chapter = get_object_or_404(MangaChapter, pk=chapterpk)
    chapter_zip = chapter.chapter
    images = {}
    
#    with ZipFile(chapter_zip, 'r') as zip:
#        for entry in zip.namelist():
#            with zip.open(entry) as file:
#            images.update({entry: base64.b64encode(zip.read(entry)),})
#                images.update({file: Image.open(file)})

    return render(request, 'manga/reader.html', {'images': images, 'chapter': chapter})