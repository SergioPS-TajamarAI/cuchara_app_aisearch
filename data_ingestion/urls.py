from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('create_company/', views.create_company, name='create_company'),
    path('map/', views.map_view, name='map_view'),
]