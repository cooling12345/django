from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def seoul(request):
    return HttpResponse("육지사람들~!")
