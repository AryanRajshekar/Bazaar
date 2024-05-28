from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def browse(request):
    # getting the items for search bar
    # request is HTTP request
    # GET is HTTP 
    # .get('query') is http get url ?query=example
    # 'query' input tag value {{query}} '' is default
    # query is the name in the url http same as category
    query = request.GET.get('query', '' )
    # gets the category part of the url which is category.id
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items=Item.objects.filter(is_sold=False)

    if category_id:
        # category_id(1) is param of this items, category_id(2) is refrencing .GET one 
        items=items.filter(category_id=category_id)
    # if query is got then it will return True 
    if query:
        # if the name contains query(i) then query is processed
        # items is all the unsold Item
                            # where the name field contains the query string
        items=items.filter(Q(name__icontains = query) | Q(description__icontains= query))

    return render(request,'item/browse.html',{
                  'items':items,
                  'query' : query,
                  'categories' : categories,
                  'category_id': int(category_id)
    })



# this is when you click on a product
def detail(request, pk):
    item=get_object_or_404(Item,pk=pk)
    # category= item.category .category is a field in models, item is the object to which the field is called
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)
    return render(request, 'item/detail.html',{
        'related_items' : related_items,
        'item': item
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            #commit False so that form isnt saved in database immediately
            # since we are redirecting back to detail we need to 
            # set item as the form so it is displayed in detail.html
            item=form.save(commit=False)

            # created_by is a field in models.py for Item
            item.created_by = request.user
            item.save()
            # after savind display details of the newly added item
            return redirect('item:detail',pk=item.id)
    else:
        form=NewItemForm()

    return render(request, 'item/form.html',{
        'form':form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    # getting the item created by an user
    item = get_object_or_404(Item, pk=pk,created_by = request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            # after savind display details of the newly added item
            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)

    return render(request, 'item/form.html',{
        'form':form,
        'title': 'Edit item',
    })

# @login_required
# def dashboard(request):
#     return render(request,'item/dashboardmine.html')
        
    