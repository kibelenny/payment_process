from django.test import TestCase
from rest_framework import status

from payments.models import Payment


# Create your tests here.
class PaymentTests(TestCase):
    def test_initiate_payment(self):
        data = {
            'amount': '100.00',
            'customer_email': 'test@email.com',
            'customer_name': 'Test User'
        }
        response = self.client.post('/api/v1/payments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('payment', response.data)
        self.assertEqual(Payment.objects.get().customer_name, 'Test User')

    def test_get_payment_status(self):
        data = {
            'amount': '100.00',
            'customer_email': 'test2@gmail.com',
            'customer_name': 'Test User2'
        }
        response = self.client.post('/api/v1/payments/', data, format='json')
        payment_id = response.data['payment']['id']
        response = self.client.get(f'/api/v1/payments/{payment_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payment']['customer_email'], 'test2@gmail.com')

    def test_incomplete_payment_data(self):
        data = {
            'amount': '100.00',
            'customer_email': 'noname@email.com',
        }
        response = self.client.post('/api/v1/payments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_missing_payment(self):
        response = self.client.get(f'/api/v1/payments/00000000-0000-0000-0000-000000000000/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Payment not found')