from rest_framework import serializers
from .models import Todo, TodoList




class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    list = serializers.CharField(max_length= 100)
    completed=serializers.BooleanField(default=False)

    def create(self, validated_data):
        return TodoList.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.list = validated_data.get("list", instance.list)
        instance.completed = validated_data.get("completed", instance.completed)
 

        instance.save()
        return instance




class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title= serializers.CharField(max_length= 100)
    generated_by = serializers.IntegerField()
    description=serializers.CharField(max_length=200)
    deadline = serializers.DateField()
    todolists = TodoListSerializer(many = True, read_only= True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.generated_by = validated_data.get("generated_by", instance.generated_by)
        instance.description = validated_data.get("description", instance.description)
        instance.deadline = validated_data.get("deadline", instance.deadline)
        instance.todolists = validated_data.get("todolists", instance.todolists)

        instance.save()
        return instance


