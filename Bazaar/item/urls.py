from django.urls import path

from . import views

app_name = 'item'
# frmo views.py the detail function is being called
urlpatterns = [
    path('<int:pk>/',views.detail, name='detail'),
    path('browse/',views.browse, name='browse'),
    path('add/', views.new,name='add'),
    #path('dashboard/', views.dashboard,name='dashboard')
    path('<int:pk>/edit/',views.edit,name='edit')
]
