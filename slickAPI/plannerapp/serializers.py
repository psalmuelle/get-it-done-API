from .models import PlannerApp
from rest_framework import serializers


class PlannerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    user = serializers.PrimaryKeyRelatedField(read_only= True, many=False)
    plan = serializers.CharField(max_length= 200)
    created_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return PlannerApp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.plan = validated_data.get("plan", instance.plan)
        instance.user = validated_data.get("user", instance.user)
        instance.created_on = validated_data.get("created_on", instance.created_on)
        instance.save()
        return instance

        