from rest_framework import serializers
from .models import ListofQuestions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListofQuestions
        fields='__all__'