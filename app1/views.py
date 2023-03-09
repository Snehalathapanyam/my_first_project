from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sneha(request):
    return HttpResponse('<h1>My First Project</h1>')