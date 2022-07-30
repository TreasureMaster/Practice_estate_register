from django.urls import path

from .views import (
    MaterialView,
    MaterialListView,
)


app_name = 'registry'

urlpatterns = [
    path('materials/', MaterialListView.as_view()),
    path('materials/<int:pk>/', MaterialView.as_view()),
]
