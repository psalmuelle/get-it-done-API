from django.contrib.auth.models import User
from .models import NoteApp
from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    title = serializers.CharField(max_length= 100)
    note = serializers.CharField(max_length=1000)
    created_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return NoteApp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.note = validated_data.get("note", instance.note)
        instance.user = validated_data.get("user", instance.user)
        instance.created_on = validated_data.get("created_on", instance.created_on)
        instance.save()
        return instance

        