from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo, TodoList
from .serializers import TodoListSerializer, TodoSerializer

#Todo Views 

@api_view(["POST"])
def create_todo(request):
    pass


@api_view(["GET"])
def get_todo(request):
    pass


@api_view(["DELETE"])
def delete_todo(request):
    pass


#TodoList views

@api_view(["POST"])
def create_todolist(request):
    pass


@api_view(["GET"])
def get_todolist(request):
    pass



@api_view(["PATCH"])
def update_todolist(request):
    pass