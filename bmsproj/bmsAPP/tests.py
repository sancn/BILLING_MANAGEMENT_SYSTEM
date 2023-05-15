from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Client

# Create your tests here.
class ClientAPITest(APITestCase):
    def setUp(self):
        self.create_url = reverse('client-list')

    def test_create_client(self):
        data = {
            'name': 'Test client1',
            'email': 'test1@example.com',
            'contact': 1234567890,
            'domain': 'sandeeepsharma.realhrsoft.com.np',
            'expiry_date': '2023-05-31',
            'organization_size': 's',
            'country': 'Nepal',
            'status': 'veri'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Test client1')

    def test_get_client(self):
        client = Client.objects.create(
            name='Test client1',
            email='test1@example.com',
            contact=1234567890,
            domain='sandeeepsharma.realhrsoft.com.np',
            expiry_date='2023-05-31',
            organization_size='s',
            country='Nepal',
            status='veri'
        )
        detail_url = reverse('client-detail', args=[client.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test client1')
        self.assertEqual(response.data['email'], 'test1@example.com')

# Testing for update client
    def test_update_client(self):
        client = Client.objects.create(
            name='Test client1',
            email='test1@example.com',
            contact=1234567890,
            domain='sandeeepsharma.realhrsoft.com.np',
            expiry_date='2023-05-31',
            organization_size='s',
            country='Nepal',
            status='veri'
        )
        update_url = reverse('client-detail', args=[client.id])
        data = {
            'name': 'Updated client',
            'email': 'updated@example.com',
        }
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(Client.objects.get().name, 'Updated client')
        self.assertEqual(Client.objects.get().email, 'updated@example.com')

#test for deleting a client
    def test_delete_client(self):
        client = Client.objects.create(
            name='Test client1',
            email='test1@example.com',
            contact=1234567890,
            domain='sandeeepsharma.realhrsoft.com.np',
            expiry_date='2023-05-31',
            organization_size='s',
            country='Nepal',
            status='veri'
        )
        delete_url = reverse('client-detail', args=[client.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)
        print(response.data)

#checking with invalid data
    def test_create_client_invalid_data(self):
        data = {
            'name': 'Test client1',
            'email': 'invalid_email',
            'contact': 'invalid_contact',
            'domain': 'sandeeepsharma.realhrsoft.com.np',
            'expiry_date': '2023-05-31',
            'organization_size': 's',
            'country': 'Nepal',
            'status': 'veri'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Client.objects.count(), 0)