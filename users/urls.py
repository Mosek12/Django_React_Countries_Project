from django.urls import path
from frontend import views
from frontend import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.blog, name='blog-blog'),
    path('rejestracja/', user_views.register, name='register'),
    path('logowanie/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('wylogowywanie/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout')
]
