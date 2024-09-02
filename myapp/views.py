from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Item

# Create your views here.
def item_list(request):
    items = Item.objects.all()

    return render(request, 'myapp/item_list.html', {'items': items})



def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {'item': item}
    return render(request, 'myapp/item_list.html', context)