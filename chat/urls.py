from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('get_file/', views.get_file, name='get_file'),
    path('menu_description/', views.menu_description, name='menu_description'),
]
