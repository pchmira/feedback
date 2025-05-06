import re
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Feedback
        fields = ['id', 'feedback_type', 'name', 'email', 'description', 'file']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно содержать минимум 2 символа.")
        if not re.match(r'^[A-Za-zА-Яа-яЁё\s\-]+$', value):
            raise serializers.ValidationError("Имя может содержать только буквы, пробелы и дефисы.")
        return value

    def validate_email(self, value):
        if re.search(r'[А-Яа-яЁё]', value):
            raise serializers.ValidationError("Email не должен содержать русские буквы.")
        return value

    def validate_description(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Описание должно содержать минимум 10 символов.")
        return value

    def validate_file(self, file):
        if file and file.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Файл не должен превышать 5MB.")
        return file
