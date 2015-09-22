#from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        #Item.objects.create(counter=request.POST['item_counter'])
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')

    
#    items = Item.objects.all()
#    counter = Item.objects.count()
#    if counter == 0:
#        comment = "yey, waktunya berlibur"
#    elif counter < 5:
#        comment = "sibuk tapi santai"
#    else:
#        comment = "oh tidak"

#    return render(request, 'home.html', {'items':items, 'comment':comment})



def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

    #if request.method == 'POST':
    #    new_item_text = request.POST['item_text'] 
    #    Item.objects.create(text=new_item_text) 
    #else:
    #    new_item_text = '' 

    #return render(request, 'home.html', {'new_item_text': new_item_text})


    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    #return HttpResponse('<html> <head><title>To-Do lists</title></head> <body><h2>Ardian - 1206208031</h2><h3>Hello World!</h3></body> </html>')
