from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo, TodoList
from .serializers import TodoListSerializer, TodoSerializer
from knox.auth import TokenAuthentication

@api_view(["POST", "GET"])
def todo(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token: 
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        if request.method == "POST":
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "GET":
            todos = Todo.objects.filter(user = request.user)
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



@api_view(["PUT"])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    
    serializer = TodoSerializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
       
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





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
def get_todolist(request):
    
    
    if request.method == "GET":
        todolist = TodoList.objects.all()
        serializer = TodoListSerializer(todolist, many=True)
        return Response(serializer.data) 