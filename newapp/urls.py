"""
URL configuration for newpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [path('',views.home,name='home'),
               path('base',views.home,name='home'),
               path('department',views.department,name='department'),
               path('doctors',views.doctors,name='doctors'),
               path('booking',views.booking,name='booking'),
               path('book',views.book,name='book'),
               path('savebooking',views.savebooking,name='savebooking'),
               path('contact',views.contactpage,name='about'),
               path('about',views.aboutpage,name='about'),
               path('register',views.toRegister,name='register'),
               path('login',views.toLogin,name='login'),
               path('adminpage',views.adminpage,name='adminpage'),
               path('success',views.success)
    
]

