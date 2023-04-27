from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('add-word', views.addword, name="addword"),
    path('dictionary', views.dictionary, name="dictionary"),
    path('news', views.news, name="news"),
    path('lessons', views.lessons, name="lessons"),
]
