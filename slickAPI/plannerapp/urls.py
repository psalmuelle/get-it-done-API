from django.urls import path
from . import views


urlpatterns = [
    path("plan/create/", views.plan),
    path("plan/get/", views.plan),
    path("plan/delete/<int:pk>/", views.delete_plan),
]
