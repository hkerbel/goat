from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')     ### GET


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})     ### GET


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')


def OBSOLETEhome_page(request):
    if request.method == 'POST':
        ###[hjk:1 - Code in book chapter 5.3 is flawed - must render via template. Apr 9 2018 ]
        ###[hjk:1] return HttpResponse(request.POST['item_text'])
        return TemplateResponse(request, 'home.html', {'new_item_text': request.POST['item_text']})

    return render(request, 'home.html')     ### GET
