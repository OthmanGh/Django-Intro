from django.http import HttpResponse

def homepage(request):
    return 'Hello From Home Page'

def about(request):
    return 'Hello from about Page'