from django.db import models

class Feedback(models.Model):
    TYPE_CHOICES = [
        ('wishlist', 'Пожелание'),
        ('problem', 'Проблема'),
        ('claim', 'Претензия'),
        ('other', 'Другое'),
    ]
    feedback_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100, blank=False, null=False, default='Anonym')
    email = models.EmailField(default='example@example.com')
    description = models.TextField()
    file = models.FileField(upload_to='feedback_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.feedback_type} - {self.created_at}"