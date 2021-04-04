from rest_framework import serializers
from questions.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question 
        fields = ('author_name','category','ask','username')
