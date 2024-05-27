from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    
# describing the fields in the table
# migrate each time you add a new class and register in admin.py
class Item(models.Model):
    # Category table is imported here so it checks which category it belongs to
    category= models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    # in item_images the images are stores. Django will create that folder
    image=models.ImageField(upload_to='item_images', blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    # Foreign Key is for many one relationship. User model is imported from django Auth
    # if you want to access all items of the User we can use the related_name param to access them
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    # auto_now_add=True current date time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    