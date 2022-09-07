from django.urls import path
from . import views


urlpatterns = [
    path("note/create/", views.note),
    path("note/get/", views.note),
    path("note/delete/<int:pk>/", views.delete_note)
]
