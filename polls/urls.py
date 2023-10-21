from django.urls import path

from . import views

urlpatterns = [
    path('surveys/', views.SurveyListCreate.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', views.SurveyDetailUpdateDelete.as_view(), name='survey-detail'),
    path('polls/', views.PollListCreate.as_view(), name='poll-list'),
    path('polls/<int:pk>/', views.PollDetailUpdateDelete.as_view(), name='poll-detail'),
]
