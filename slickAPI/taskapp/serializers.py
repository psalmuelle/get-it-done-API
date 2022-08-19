from rest_framework import serializers
from .models import Todo, TodoList


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title= serializers.CharField(max_length= 100)
    description=serializers.CharField(max_length=200)
    deadline = serializers.DateField()
    todolists =serializers

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.deadline = validated_data.get("deadline", instance.deadline)
        instance.todolists = validated_data.get("todolists", instance.todolists)

        instance.save()
        return instance



class TodoListSerializer(serializers.Serializer):
    list = serializers.CharField(max_length= 100)
    completed=serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.deadline = validated_data.get("deadline", instance.deadline)
        instance.todolists = validated_data.get("todolists", instance.todolists)

        instance.save()
        return instance