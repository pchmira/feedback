from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from feedback.views import FeedbackAPIView


def redirect_to_feedback(request):
    return redirect('feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_feedback, name='home'),
    path('feedback/', include('feedback.urls')),
    path('api/feedback/', FeedbackAPIView.as_view(), name='api-feedback'),  # <--- добавь это
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)