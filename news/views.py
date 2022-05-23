from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def old(request):
    news = News.objects.all()
    resp = ''
    for i in news:
        resp += f'<h2>{i.title}</h2><br><p>{i.content}</p><hr>'
    return HttpResponse(resp)


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'News list',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'current_category': current_category}
    return render(request, 'news/category.html', context)




