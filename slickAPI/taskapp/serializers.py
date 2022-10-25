from rest_framework import serializers
from .models import Todo, TodoList





class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title= serializers.CharField(max_length= 100)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    description=serializers.CharField(max_length=200)
    deadline = serializers.DateField()
  

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
   


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.user = validated_data.get("user", instance.user)
        instance.description = validated_data.get("description", instance.description)
        instance.deadline = validated_data.get("deadline", instance.deadline)
      
      
        instance.save()
        return instance





class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    list = serializers.CharField(max_length= 100)
    completed=serializers.BooleanField(default=False)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    todo = serializers.PrimaryKeyRelatedField(read_only =True)
    

    def create(self, validated_data):
        return TodoList.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.list = validated_data.get("list", instance.list)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.user = validated_data.get("user", instance.user)
        instance.todo = validated_data.get("todo", instance.todo)


        instance.save()
        return instance

