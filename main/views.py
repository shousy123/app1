from django.shortcuts import render
from django.shortcuts import HttpResponse

from goods.models import Categories

def index(request):


    context = {

        'title': 'DRY Tech - Главная',
        'content': 'DRY Tech',

    }

    return render(request, 'main/index.html', context) 

def about(request):

    context = {

        'title': 'DRY Tech - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой хороший и товар такой крутой',


    }

    return render(request, 'main/about.html', context) 