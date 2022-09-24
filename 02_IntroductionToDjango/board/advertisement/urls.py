from django.urls import path
from . import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('anxiety/', views.anxiety_detail, name='advertisement_list'),
    path('python/', views.python_detail, name='advertisement_list'),
    path('russian/', views.russian_detail, name='advertisement_list'),
    path('SQL/', views.SQL_detail, name='advertisement_list'),
    path('web/', views.web_detail, name='advertisement_list')
]