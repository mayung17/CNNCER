from django.shortcuts import render,redirect
from .models import Patient

def home(request):
    return render(request,"index.html")