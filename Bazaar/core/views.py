from django.shortcuts import render, redirect
# importing from the folder where you created item and category
from item.models import Category, Item
from .forms import SignupForm
# Create your views here.



def index(request):
    # core is the folder name inside template and this line has sepcified the path
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    # foldername (templatesname)/ webpage.html
    return render(request,'core/contact.html')

def loggedin(request):
    # core is the folder name inside template and this line has sepcified the path
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/loggedin.html',{
        'categories' : categories,
        'items' : items,
    })

def signup(request):
    if request.method=='POST':
        # this makes it so that the class SignUpForm takes post request
        # form = SignupForm(attributes_of_a_class = '-')
        # form is an object
        
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            # the /login/ is the path in settings.py Login_url
            return redirect('/login/')
    else:
        # initial look of the page if theres no request
        form = SignupForm()

    return render(request,'core/signup.html',{
       # will be used in html
        'form': form
    })

