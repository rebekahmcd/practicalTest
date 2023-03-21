from django.shortcuts import render
from weather.models import News

def page(request):
    news = News.objects.all()
    return render(request, 'weather/page.html', {'news': news})