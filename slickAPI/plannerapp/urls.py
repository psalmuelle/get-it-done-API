from django.urls import path
from . import views


urlpatterns = [
    path("planner/create", views.create_note),
    path("planner/get", views.get_note),
    path("planner/delete/<int:pk>", views.delete_note)
]
