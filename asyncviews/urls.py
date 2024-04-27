"""
URL configuration for asyncviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from django.urls import path
from django.urls import path
from . import views  # Importa as views do mesmo aplicativo

# Define as rotas para o projeto
urlpatterns = [
    path('time_counter/', views.async_time_counter, name='time_counter'),  # Rota para a view assíncrona
    path('api/', views.api, name='api'),  # Rota para a view padrão
    path('async_http/', views.async_view, name='async_http')  # Rota para a função assíncrona de chamadas HTTP
]


