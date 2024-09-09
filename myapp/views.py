from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('Create Something')

def read(request, id):
    return HttpResponse('read'+id)