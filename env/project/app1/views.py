from django.shortcuts import render

# Create your views here.


def Home(req):
    return render(req,"index.html")

def About(req):
    return render(req,'about.html')