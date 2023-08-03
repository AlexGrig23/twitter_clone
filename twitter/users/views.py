from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse("Hello world!!!")


def test(request):
    print(dir(request))
    return HttpResponse("<h1>test title</h1>")