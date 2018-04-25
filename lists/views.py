from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.forms import ItemForm
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})

    # # # list_ = List.objects.create()    
    # # # item = Item.objects.create(text=request.POST['text'], list=list_)
    # # # ####item = Item.objects.create(text=request.POST['item_text'], list=list_)
    
    # # # try:
    # # #     item.full_clean()
    # # # except ValidationError:
    # # #     list_.delete()
    # # #     error = "You can't have an empty list item"
    # # #     return render(request, 'home.html', {'error': error})
    
    # # # return redirect(list_)      # Utilizes get_absolute_url.


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)

    return render(request, 'list.html', {'list': list_, 'form': form})

