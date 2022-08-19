from .models import PlannerApp
from rest_framework import serializers


class PlannerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    plan = serializers.CharField(max_length= 200)
    generated_by = serializers.IntegerField()
    created_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return PlannerApp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.plan = validated_data.get("plan", instance.plan)
        instance.generated_by = validated_data.get("generated_by", instance.generated_by)
        instance.created_on = validated_data.get("created_on", instance.created_on)
        instance.save()
        return instance

        