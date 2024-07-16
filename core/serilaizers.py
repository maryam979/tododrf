from rest_framework import serializers

from core.models import Todo

class TodoSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            "title",
            'content',
            'image'
        ]