from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index/homepage.html", {})


def forms(request):
    return render(request, "index/forms.html", {})