from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})     ### GET


def OBSOLETEhome_page(request):
    if request.method == 'POST':
        ###[hjk:1 - Code in book chapter 5.3 is flawed - must render via template. Apr 9 2018 ]
        ###[hjk:1] return HttpResponse(request.POST['item_text'])
        return TemplateResponse(request, 'home.html', {'new_item_text': request.POST['item_text']})

    return render(request, 'home.html')     ### GET
