from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo, TodoList
from .serializers import TodoListSerializer, TodoSerializer

#Todo Views 

@api_view(["POST"])
def create_todo(request):
    
    if request.method == "POST":
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_todo(request,pk):
    generated_by = pk
    if request.method == "GET":
        todos = Todo.objects.filter(generated_by = generated_by)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data) 

@api_view(["DELETE"])
def delete_todo(request,pk):
    try:
        todos = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    todos.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#TodoList views

@api_view(["POST"])
def create_todolist(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
def update_todolist(request, pk):
    todo = TodoList.objects.get(pk=pk)
    serializer = TodoListSerializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_todolist(request,pk):
    todo_id = pk
    if request.method == "GET":
        todolist = TodoList.objects.filter(todo_id = todo_id)
        serializer = TodoListSerializer(todolist, many=True)
        return Response(serializer.data) 