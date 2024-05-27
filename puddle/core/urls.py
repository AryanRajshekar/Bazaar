from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    # path('route', what to display in route, unique name)
    # what to display is filename.functionname
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    # this is default model from Django hence not defined in views.py
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    # loggedin same as index.html but with welcome user
    # user is login_redirected_url
    path('user/',views.loggedin,name='loggedin'),
    
    # default model from django
    path('logout/',LogoutView.as_view(),name='logout')
]
