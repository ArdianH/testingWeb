from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    Item.objects.create(counter=request.POST['item_counter'])
    #    return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

    
    #items = Item.objects.all()
    #counter = Item.objects.count()
    #if counter == 0:
    #    comment = "yey, waktunya berlibur"
    #elif counter < 5:
    #    comment = "sibuk tapi santai"
    #else:
    #    comment = "oh tidak"

    #return render(request, 'list.html', {'items':items, 'comment':comment})



def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    #items = Item.objects.all()
    #items = Item.objects.filter(id=list_id)
    #counter = List.objects.filter(id=list_id).count()
    #counter = Item.objects.count
    counter = list_.item_set.count()
    #counter = 0
    #for item in list_.item_set.all():
    #    counter += 1
    #endfor

    if counter == 0:
        comment = "yey, waktunya berlibur"
    elif counter < 5:
        comment = "sibuk tapi santai"
    else:
        comment = "oh tidak"

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id,))
        except ValidationError:
            error = "You can't have an empty list item"

    #return render(request, 'list.html', {'list': list_})
    return render(request, 'list.html', {'list':list_, 'error':error, 'comment':comment})

    #return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id,))
    #return redirect('/lists/the-only-list-in-the-world/')


#def add_item(request, list_id):
#    list_ = List.objects.get(id=list_id)
#    Item.objects.create(text=request.POST['item_text'], list=list_)
#    return redirect('/lists/%d/' % (list_.id,))
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
