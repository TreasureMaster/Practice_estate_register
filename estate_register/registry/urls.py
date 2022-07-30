from django.urls import path

from .views import (
    MaterialView,
    MaterialListView,
    TargetView,
    TargetListView,
    DeaneryView,
    DeaneryListView,
)


app_name = 'registry'

urlpatterns = [
    path('materials/', MaterialListView.as_view()),
    path('materials/<int:pk>/', MaterialView.as_view()),
    path('targets/', TargetListView.as_view()),
    path('targets/<int:pk>/', TargetView.as_view()),
    path('deans/', DeaneryListView.as_view()),
    path('deans/<int:pk>/', DeaneryView.as_view()),
]
