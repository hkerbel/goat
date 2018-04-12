from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')     ### GET


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})     ### GET


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')


def OBSOLETEhome_page(request):
    if request.method == 'POST':
        ###[hjk:1 - Code in book chapter 5.3 is flawed - must render via template. Apr 9 2018 ]
        ###[hjk:1] return HttpResponse(request.POST['item_text'])
        return TemplateResponse(request, 'home.html', {'new_item_text': request.POST['item_text']})

    return render(request, 'home.html')     ### GET
