from rest_framework import serializers
from .models import Skate


class SkateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "category", "review", "created_at", "update_at")
        model = Skate
