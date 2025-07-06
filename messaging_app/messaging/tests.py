from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Message


class MessageModelTest(TestCase):
    """Test cases for Message model."""

    def setUp(self):
        """Set up test data."""
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='test1@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )

    def test_message_creation(self):
        """Test creating a message."""
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            content='Hello, this is a test message!'
        )
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.recipient, self.user2)
        self.assertEqual(message.content, 'Hello, this is a test message!')
        self.assertFalse(message.is_read)

    def test_message_str_representation(self):
        """Test string representation of message."""
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            content='Test message'
        )
        self.assertIn(self.user1.username, str(message))
        self.assertIn(self.user2.username, str(message))


class MessageAPITest(APITestCase):
    """Test cases for Message API."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='test1@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user1)

    def test_create_message(self):
        """Test creating a message via API."""
        url = reverse('message-list')
        data = {
            'recipient': self.user2.id,
            'content': 'Hello from API!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        message = Message.objects.first()
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.recipient, self.user2)
        self.assertEqual(message.content, 'Hello from API!')

    def test_list_messages(self):
        """Test listing messages."""
        # Create a message
        Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            content='Test message'
        )
        url = reverse('message-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_mark_message_as_read(self):
        """Test marking a message as read."""
        message = Message.objects.create(
            sender=self.user2,
            recipient=self.user1,
            content='Test message'
        )
        url = reverse('message-mark-as-read', kwargs={'pk': message.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        message.refresh_from_db()
        self.assertTrue(message.is_read)

    def test_unauthorized_mark_as_read(self):
        """Test marking a message as read by wrong user."""
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            content='Test message'
        )
        url = reverse('message-mark-as-read', kwargs={'pk': message.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserAPITest(APITestCase):
    """Test cases for User API."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_users(self):
        """Test listing users."""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_user(self):
        """Test retrieving a specific user."""
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username) 