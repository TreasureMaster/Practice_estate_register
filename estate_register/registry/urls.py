from django.urls import path

from .views import (
    MaterialResource,
    MaterialListResource,
    TargetResource,
    TargetListResource,
    DeaneryResource,
    DeaneryListResource,
)


app_name = 'registry'

urlpatterns = [
    path('materials/', MaterialListResource.as_view()),
    path('materials/<int:pk>/', MaterialResource.as_view()),
    path('targets/', TargetListResource.as_view()),
    path('targets/<int:pk>/', TargetResource.as_view()),
    path('deans/', DeaneryListResource.as_view()),
    path('deans/<int:pk>/', DeaneryResource.as_view()),
]
