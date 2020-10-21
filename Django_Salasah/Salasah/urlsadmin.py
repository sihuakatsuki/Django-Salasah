from django.urls import path
from .import viewsadmin

urlpatterns = [
    path('Backend/',viewsadmin.home, name= 'home'),
    path('list/', viewsadmin.produk_list, name = 'list-produk'),
    path('create/', viewsadmin.produk_create, name='create-produk'),

]