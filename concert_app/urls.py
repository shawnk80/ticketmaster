from django.urls import path
from . import views

app_name = 'concert_app'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('search/', views.search_results, name='search_results'),
]
