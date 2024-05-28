from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from item.models import Item

# Create your views here.


@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)


        # necessary to create key of the thing you wanted to access at render
    return render(request,'dashboard/index.html',{
        'items' : items,
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)
    item.delete()  
    # since there are 2 index.html it wont know which is which
    return redirect('dashboard:index')