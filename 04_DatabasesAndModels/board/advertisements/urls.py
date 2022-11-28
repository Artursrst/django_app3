from django.urls import path
from . import views
from .views import AdvertisementsListView, AdvertisementsDetailView

urlpatterns = [
    path('advertisements/', views.AdvertisementsListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', views.AdvertisementsDetailView.as_view(), name='advertisements-detail')
]
