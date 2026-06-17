from rest_framework import serializers
from .models import Task

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")
        if len(value) > 255:
            raise serializers.ValidationError("Title cannot exceed 255 characters.")
        return value

    def validate_status(self, value):
        allowed = ['pending', 'in_progress', 'completed']
        if value not in allowed:
            raise serializers.ValidationError(f"Status must be one of: {', '.join(allowed)}")
        return value

    def validate(self, data):
        if 'title' in data and 'description' in data:
            if data['title'].lower() == data['description'].lower():
                raise serializers.ValidationError("Title and description cannot be the same.")
        return data