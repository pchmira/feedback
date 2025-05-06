from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Feedback

class FeedbackAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/feedback/'
        self.valid_data = {
            'feedback_type': 'problem',
            'name': 'Алексей',
            'email': 'user@example.com',
            'description': 'Это описание не короче 10 символов.',
        }

    def test_invalid_name_with_numbers(self):
        data = self.valid_data.copy()
        data['name'] = 'Alex123'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_invalid_email_with_cyrillic(self):
        data = self.valid_data.copy()
        data['email'] = 'почта@пример.рф'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_file_too_large(self):
        big_file = SimpleUploadedFile("bigfile.txt", b"a" * (5 * 1024 * 1024 + 1))
        data = self.valid_data.copy()
        data['file'] = big_file
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)

    def test_description_too_short(self):
        data = self.valid_data.copy()
        data['description'] = 'коротко'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('description', response.data)

    def test_missing_required_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('feedback_type', response.data)
        self.assertIn('name', response.data)
        self.assertIn('email', response.data)
        self.assertIn('description', response.data)

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
