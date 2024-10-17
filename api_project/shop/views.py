from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

def hola_mundo(request):
    return HttpResponse("Hola Mundo")



class ShopListController(View):
    def get(self, request):
        return HttpResponse("Hola Mundo")

