from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog_news, Categories
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def show_home_page(request):
    return render(request, "main/home.html", {'News':Blog_news.objects.all})

def show_categories(request):
    return render(request, "main/categories.html",{'category': Categories.objects.all})


def separator(request, url_slug):
    category_urls=[c.url_slug for c in Categories.objects.all()]
    if url_slug in category_urls:
        posts=Blog_news.objects.filter(news_category__url_slug=url_slug)
        return render(request, "main/home.html", {"News":posts})

    if url_slug in [c.url_slug_news for c in Blog_news.objects.all()]:
        article = Blog_news.objects.get(url_slug_news=url_slug)
        return render(request, "main/article.html", {"article":article})
        

        
    return HttpResponse("Not a category")



def register_(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data["username"]
            messages.success(request,f"Ви ввійшли як {username}")
            return redirect("main:home")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form=UserCreationForm
    return render(request, "main/registrations.html", {"form":form})


def logout_(request):
    logout(request)
    messages.info(request, "Ви вийшли зі свого аккаунту!")
    return redirect("main:home")


def login_(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Ви ввійшли як {username}")
                return redirect("main:home")
            else:
                messages.info(request, f"""Немає такого користувача {username}, або неправильний пароль {password}""")
        else:
            messages.error(request, f"""Неправильне ім'я або пароль!!!""")
    form= AuthenticationForm
    return render(request, "main/login.html", {"form":form})


def show_article(request, id_):
    return HttpResponse("%s" %id)

def show_for_customer(request):
    pass

def show_for_customer(request,number):
    return HttpResponse("""<h1>Hello Customer %s!!!</h1> <p><strong>You are welcome!</p>""" % number)