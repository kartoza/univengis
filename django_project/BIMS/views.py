# coding=UTF-8
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the BIMS app landing page. Please go to /admin/ for more")

