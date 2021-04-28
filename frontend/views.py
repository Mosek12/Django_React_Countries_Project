from django.shortcuts import redirect, render
from users.forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render
from blog.models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'frontend/home.html', context)


def informacje(request):
    context = {
        'title': 'Informacje',
        'posts': Post.objects.all()
    }
    return render(request, 'frontend/informacje.html', context)


def blog(request):
    context = {
        'title': 'Blog',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/main.html', context)


def kuchnia(request):
    context = {
        'title': 'Kuchnia',
        'posts': Post.objects.all()
    }
    return render(request, 'frontend/kuchnia.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Twoje konto zostało stworzone! Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'title': 'Rejestracja',
               'form': form}
    return render(request, 'users/register.html', context)
