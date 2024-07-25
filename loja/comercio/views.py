from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def cadastrar(request):

    produto = Produto.objects.filter(nome__contains="ana", preco=30)
    return HttpResponse(produto)
