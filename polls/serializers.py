from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Survey, Poll


class SurveySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Survey
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Poll
        fields = '__all__'
