from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('informacje/', views.informacje, name='blog-informacje'),
    path('kuchnia/', views.kuchnia, name='blog-kuchnia')
]
