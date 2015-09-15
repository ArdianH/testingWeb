from django.shortcuts import render
#from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')   
# return HttpResponse('<html> <head><title>To-Do lists</title></head> <body><h2>Ardian - 1206208031</h2><h3>Hello World!</h3></body> </html>')
