from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView

from .form import ItemForm
from .models import Item

# Create your views here.

def item(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    # template = loader.get_template('food/index.html')
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {'item':item}
    return render(request,'food/detail.html',context)

class DetailView(DetailView):
    model = Item
    template_name ='food/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    def form_valid(self, form):
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form':form, 'item':item})

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})