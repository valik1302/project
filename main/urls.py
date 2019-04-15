"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from.import views
app_name= 'main'

urlpatterns = [
    path("", views.show_categories, name='home'),
    path("customer<int:number>", views.show_for_customer, name="show"),
    path("article<int:id_>",views.show_article),
    path("register", views.register_),
    path("login", views.login_),
    path("logout", views.logout_),
    path("<slug:url_slug>", views.separator)

]
