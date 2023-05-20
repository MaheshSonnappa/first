from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>This is my First FBV</h1>")

def second(request):
    return HttpResponse("<h1>This is my second FBV</h1>")

def third(request):
    return HttpResponse("<h1>This is my Third FBV</h1>")
def fourth(request):
    return HttpResponse("<h1>This is my Fourth FBV</h1>")

def fifth(request):
    return HttpResponse("<h1 style='color: red;'>This is my Fifth FBV</h1>")

def sixth(request):
    return HttpResponse("<input type='password' placeholder='password' style='padding: 12px; width: 500px;'>")
