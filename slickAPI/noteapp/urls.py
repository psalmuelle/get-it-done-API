from django.urls import path
from . import views


urlpatterns = [
    path("note/create/", views.create_note),
    path("note/get/", views.get_note),
    path("note/delete/<int:pk>/", views.delete_note)
]
