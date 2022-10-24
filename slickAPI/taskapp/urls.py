from django.urls import path
from . import views


urlpatterns= [
path("todo/create/",views.todo),
path("todo/get/", views.todo),
path("todo/update/<int:pk>/", views.update_todo),
path("todo/delete/<int:pk>/", views.delete_todo),
path("todolist/create/", views.create_todolist),
path("todolist/update/<int:pk>/", views.update_todolist),
path("todolist/get/", views.get_todolist),


]