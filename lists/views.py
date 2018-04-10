from django.http import HttpResponse
from django.shortcuts import render

from django.template.response import TemplateResponse ###[hjk:1]

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
###    return render(request, 'home.html', {'new_item_text': request.POST['item_text']})

def OBSOLETEhome_page(request):
    if request.method == 'POST':
        ###[hjk:1 - Code in book chapter 5.3 is flawed - must render via template. Apr 9 2018 ]
        ###[hjk:1] return HttpResponse(request.POST['item_text'])
        return TemplateResponse(request, 'home.html', {'new_item_text': request.POST['item_text']})

    return render(request, 'home.html')     ### GET
