from django.shortcuts import render, redirect
from .models import Word, News, Lessons
from .forms import WordForm
from django.views.generic import DetailView

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def addword(request):
    error = ''
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary')
        else:
            error = 'Ошибка при использовании формы'

    form = WordForm()
    context = {
        'form':  form,
        'error': error
    }
    return render(request, "main/addword.html", context)

def dictionary(request):
    words = Word.objects.order_by('word')
    return render(request, "main/dictionary.html", {'title': 'Словарь', 'words': words})

def news(request):
    new = News.objects.order_by('-id')
    return render(request, "main/news.html", {'title': 'Новости', 'news': new})

def lessons(request):
    lesson = Lessons.objects.order_by('-date')
    return render(request, "main/lessons.html", {'title': 'Уроки', 'lessons': lesson})

