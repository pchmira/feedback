from django.urls import path
from .views import FeedbackAPIView, feedback_form_view

urlpatterns = [
    path('api/feedback/', FeedbackAPIView.as_view(), name='feedback-api'),
    path('', feedback_form_view, name='feedback'),
]