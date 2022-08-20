from django.urls import path
from . import views


urlpatterns= [
path("todo/create/",views.create_todo),
path("todo/get/<int:pk>/", views.get_todo),
path("todo/delete/<int:pk>/", views.delete_todo),
path("todolist/create/", views.create_todolist),
path("todolist/update/<int:pk>/", views.update_todolist)


]