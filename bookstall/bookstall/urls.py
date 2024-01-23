"""
URL configuration for bookstall project.

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
from django.contrib import admin
from django.urls import path
from books import views
# localhosts:8000/books/all/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/all',views.BookListView.as_view(),name="book-list"),
    path('books/<int:pk>/',views.BookDetailsView.as_view(),name="book-details"),
    path('books/<int:pk>/remove/',views.BookDeleteView.as_view(),name="book-delete"),
    path("books/add/",views.BookCreateView.as_view(),name="book-add"),
]

