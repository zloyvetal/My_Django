from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'SERHEY'
    our_context = {'date': date, 'name': name}

    return render(request, 'home.html', our_context)
