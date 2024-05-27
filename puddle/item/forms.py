from django import forms
from .models import Item


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"

class NewItemForm(forms.ModelForm):
    class Meta:
        # necessary to assign a model in py files that are in models.py to let Django know
        # by assigning this the class is referenced to Item class and its attributes
        model=Item
        # these fields become headings by default when you create a model
        # must be same as fields in model created
        fields = ('category','name', 'description','price', 'image')

        # forms.Select creates a drop down option
        # easier to set CSS for each widget in this case
        widgets = {
            'category': forms.Select(attrs={
            'class' : INPUT_CLASSES
        }),
            'name': forms.TextInput(attrs={
            'class' : INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
            'class' : INPUT_CLASSES
        }),
            'price': forms.TextInput(attrs={
            'class' : INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
            'class' : INPUT_CLASSES
        }),
        } 
    
class EditItemForm(forms.ModelForm):
    class Meta:
        # necessary to assign a model in py files that are in models.py to let Django know
        # by assigning this the class is referenced to Item class and its attributes
        model=Item
        # these fields become headings by default when you create a model
        fields = ('name', 'description','price', 'image', 'is_sold')

        # forms.Select creates a drop down option
        # easier to set CSS for each widget in this case
        widgets = {
            'name': forms.TextInput(attrs={
                # tailwind can be used
            'class' : INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
            'class' : INPUT_CLASSES
        }),
            'price': forms.TextInput(attrs={
            'class' : INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
            'class' : INPUT_CLASSES
        }),
        } 
    