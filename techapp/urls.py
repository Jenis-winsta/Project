from . import views
from django.urls import path

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name="login1"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register',views.register,name='register'),
    path('logout',views.logout, name='logout'),
    path('index',views.index, name='index'),
    # path('button_page',views.button_page, name='button_page')

]