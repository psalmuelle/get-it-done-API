
from .models import NoteApp
from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title = serializers.CharField(max_length= 100)
    generated_by = serializers.IntegerField()
    created_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return NoteApp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.generated_by = validated_data.get("generated_by", instance.generated_by)
        instance.created_on = validated_data.get("created_on", instance.created_on)
        instance.save()
        return instance

        