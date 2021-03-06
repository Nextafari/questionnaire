from rest_framework import serializers
from .models import (
    MultiChoiceQuestions, MultiChoiceUser, MultiChoiceAnswer
)


class GetUserSerializer(serializers.ModelSerializer):
    """Serializers for getting the user details"""
    class Meta:
        model = MultiChoiceUser
        fields = [
            "first_name", "last_name", "occupation", "highest_education",
            "phone_number", "address", "postal_code", "marital_status"
        ]


class GetAllQuestionsSerializer(serializers.ModelSerializer):
    """Get all Questions"""
    class Meta:
        model = MultiChoiceQuestions
        fields = [
            "question"
        ]


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiChoiceAnswer
        fields = [
            "answers"
        ]
