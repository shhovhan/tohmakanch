"""tohmakanch_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import HomeView
from api.views import (BiographyViewSet,
                       PoemViewSet,
                       ArticleViewSet, 
                       StoryViewSet,
                       FavouriteViewSet)


urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api/biography', BiographyViewSet.as_view({
        'get': 'list',
    })),
    path('api/articles/', ArticleViewSet.as_view({'get': 'list'})),
    path('api/articles/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve'})),
    path('api/poems/', PoemViewSet.as_view({'get': 'list'})),
    path('api/poems/<int:pk>/', PoemViewSet.as_view({'get': 'retrieve'})),
    path('api/stories/', StoryViewSet.as_view({'get': 'list'})),
    path('api/stories/<int:pk>/', StoryViewSet.as_view({'get': 'retrieve'})),
    path('api/favourites/', FavouriteViewSet.as_view({'get': 'list'})),
    path('api/favourites/<int:pk>/', FavouriteViewSet.as_view({
        'get': 'retrieve'})),
]
