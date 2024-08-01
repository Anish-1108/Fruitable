"""
URL configuration for myproject2 project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('shop-detail', views.shopdetail, name='shop-detail'),
    path('cart', views.cart, name='cart'),
    path('chackout', views.chackout, name='chackout'),
    path('Add_address', views.Add_address, name='Add_address'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('404', views.hhh, name='404'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    path('categories/<int:id>', views.categories, name='categories'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('deletes_cart/<int:id>', views.deletes_cart, name='deletes_cart'),
    path('plus/<int:id>', views.plus, name='plus'),
    path('minus/<int:id>', views.minus, name='minus'),
    path('change_address', views.change_address, name='change_address'),
    path('search', views.search, name='search')

]