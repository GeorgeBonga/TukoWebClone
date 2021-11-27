from django.shortcuts import render
from tuko.models import Post
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'tuko.html')
