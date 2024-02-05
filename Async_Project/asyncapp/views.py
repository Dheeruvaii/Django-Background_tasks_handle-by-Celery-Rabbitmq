from django.shortcuts import render

# Create your views here.
from .tasks import add
from django.http import HttpResponse

def my_view(request):
    result=add.delay(4,6)
    return HttpResponse(result)
    