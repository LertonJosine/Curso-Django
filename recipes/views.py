from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Pagina inicial")


def sobre(request):
    return HttpResponse("Sobre")

    
def contacto(request):
    return HttpResponse("Contacto")