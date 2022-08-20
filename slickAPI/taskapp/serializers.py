from email.policy import default
from rest_framework import serializers
from .models import Todo, TodoList



class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title= serializers.CharField(max_length= 100)
    generated_by = serializers.IntegerField()
    description=serializers.CharField(max_length=200)
    deadline = serializers.DateField()
   

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.generated_by = validated_data.get("generated_by", instance.generated_by)
        instance.description = validated_data.get("description", instance.description)
        instance.deadline = validated_data.get("deadline", instance.deadline)

        instance.save()
        return instance




class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    list = serializers.CharField(max_length= 100)
    completed=serializers.BooleanField(default=False)
    todo_id = serializers.IntegerField()

    def create(self, validated_data):
        return TodoList.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.list = validated_data.get("list", instance.list)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.todo_id = validated_data.get("todo_id", instance.todo_id)
 

        instance.save()
        return instance



{
"title": "Create an editable content on the social media platform",
"generated_by": "1",
"description": "You are who you are yesterday, today and forever more, I am grateful",
"deadline": "2022-12-03"
}

{
    "id": 1,
    "title": "Create an editable content on the social media platform",
    "generated_by": 1,
    "description": "You are who you are yesterday, today and forever more, I am grateful",
    "deadline": "2022-12-03"
}