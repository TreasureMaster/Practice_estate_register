from django.urls import path

from .views import (
    MaterialResource,
    MaterialListResource,
    TargetResource,
    TargetListResource,
    DeaneryResource,
    DeaneryListResource,
    DepartmentResource,
    DepartmantListResource,
    BuildingResource,
    BuildingListResource,
    HallResource,
    HallListResource,
)


app_name = 'registry'

urlpatterns = [
    path('materials/', MaterialListResource.as_view()),
    path('materials/<int:pk>/', MaterialResource.as_view()),
    path('targets/', TargetListResource.as_view()),
    path('targets/<int:pk>/', TargetResource.as_view()),
    path('deans/', DeaneryListResource.as_view()),
    path('deans/<int:pk>/', DeaneryResource.as_view()),
    path('departments/', DepartmantListResource.as_view()),
    path('departments/<int:pk>/', DepartmentResource.as_view()),
    path('buildings/', BuildingListResource.as_view()),
    path('buildings/<int:pk>/', BuildingResource.as_view()),
    path('halls/', HallListResource.as_view()),
    path('halls/<int:pk>/', HallResource.as_view()),
]
