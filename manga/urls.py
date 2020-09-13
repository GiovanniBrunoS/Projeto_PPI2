from django.urls import path
from . import views

urlpatterns = [
    path('', views.manga_list, name='manga_list'),
    path('<int:pk>/', views.manga_detail, name='manga_detail'),
    path('new-manga/', views.manga_new, name='manga_new'),
    path('<int:pk>/edit/', views.manga_edit, name='manga_edit'),
    path('<int:pk>/remove/', views.manga_remove, name='manga_remove'),
    path('<int:pk>/new_chapter/', views.chapter_new, name='chapter_new'),
    path('<int:mangapk>/<int:chapterpk>', views.reader, name='reader'),
]