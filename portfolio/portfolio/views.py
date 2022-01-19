from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    text = {
        'name': 'Sean Shea',
        'age': 26,
        'phone': 7814700262,
        'friend_name': ['Bob', 'Joe', 'Jane', 'John']
    }
    return render(request, 'index.html', text)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')