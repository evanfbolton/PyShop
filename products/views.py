from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello, word')


def new(request):
    return HttpResponse('New Products')


