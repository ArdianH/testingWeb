from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse('<html> <head><title>To-Do lists</title></head> <body><h1>Ardian - 1206208031</h1><h3>Hello World!</h3></body> </html>')
