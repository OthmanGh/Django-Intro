# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("Hello World From Home Page")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse('Hello From About page')
    return render(request, 'about.html')