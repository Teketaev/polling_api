from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Survey, Poll
from .permissions import OwnerAdminOrReadOnly
from .serializers import SurveySerializer, PollSerializer


class SurveyListCreate(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (IsAuthenticated,)


class SurveyDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (OwnerAdminOrReadOnly,)


class PollListCreate(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated,)


class PollDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (OwnerAdminOrReadOnly,)
