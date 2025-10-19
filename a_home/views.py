from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_view(request):
    items_list = Item.objects.all()
    context = {"items": items_list}
    return render(request, 'home.html', context=context)


def create_item(request):
    if request.POST:
        name = request.POST.get('name')
        item = Item(name=name)
        item.save()
        return HttpResponse(f'<li class="text-8xl font-thin">{item.name}</li>')
    else:
        return redirect('home')