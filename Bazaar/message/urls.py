from django.urls import path
from . import views
app_name = 'message'

urlpatterns = [
    path('', views.inbox,name='inbox'),
    path('<int:pk>/',views.detail,name='detail')
]