from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse("Coming soon")


def test(request):
    print(dir(request))
    return HttpResponse("<h1>Hello Alex</h1>")
