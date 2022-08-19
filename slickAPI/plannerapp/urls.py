from django.urls import path
from . import views


urlpatterns = [
    path("plan/create/", views.create_plan),
    path("plan/get/", views.get_plan),
    path("plan/delete/<int:pk>/", views.delete_plan),
]
