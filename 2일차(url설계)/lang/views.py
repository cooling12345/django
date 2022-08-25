from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def c(request):
    return HttpResponse("hello c")

def python(request):
    return HttpResponse("hello python")

def java(request):
    return HttpResponse("hello java")