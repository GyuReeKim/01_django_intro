from django.shortcuts import render
import random
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request):
    menu = ['중식', '한식', '양식']
    pick = random.choice(menu)

    context = {
        'pick': pick,
        'menu': menu,
    }
    return render(request, 'dinner.html', context)

def image(request):
    pick = random.choice(range(10))
    context = {
        'img_url': f'https://picsum.photos/id/{pick}/200/300',
    }
    return render(request, 'image.html', context)

def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)

def cube(request, num):
    cubic = num ** 3
    context = {
        'num': num,
        'cubic': cubic
    }
    return render(request, 'cube.html', context)

def mul(request, num1, num2):
    context = {
        'result': num1*num2,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'mul.html', context)

def dtl(request):
    menus = ['한식', '중식', '양식', '일식']
    sentence = 'Life is short you need python'
    messages = {
        'apple': '사과',
        'banana': '바나나',
        'peach': '복숭아',
    }
    now = datetime.datetime.now()
    empty = []

    context = {
        'now': now,
        'messages': messages,
        'sentence': sentence,
        'menus': menus,
        'empty': empty,
    }
    return render(request, 'dtl.html', context)

def christmas(request):
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    
    today = f'{month}/{day}'

    if today == '12/25':
        is_christmas = True
    else:
        is_christmas = False
    
    context = {
        'is_christmas': is_christmas,
    }
    return render(request, 'christmas.html', context)
