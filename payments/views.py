import uuid

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from payments.models import Payment
from payments.serializers import PaymentSerializer, PaymentStatusSerializer
from rest_framework import status


# Create your views here.
class InitializePayment(GenericAPIView):
    serializer_class = PaymentSerializer
    
    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            payment = serializer.save()
            # At this point, you would typically integrate with a payment gateway and receive an ID back
            payment.provider_id = str(uuid.uuid4())
            payment.save()
            return Response({
                'payment': {
                    'id' : str(payment.id),
                    'amount': str(payment.amount),
                    'customer_email': payment.customer_email,
                    'customer_name': payment.customer_name,
                    'status': payment.status,
                },
                'status': 'Payment initialized successfully',
                'message': 'Payment Initialized Successfully',
            }, status=status.HTTP_201_CREATED)
        return Response({
            'errors': serializer.errors,
            'message': 'Failed to initialize payment',
        }, status=status.HTTP_400_BAD_REQUEST,
        )
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response({
            'payments': serializer.data,
            'status': 'success',
            'message': 'Payments Retrieved Successfully',
        }, status=status.HTTP_200_OK)

class PaymentStatus(GenericAPIView):
    serializer_class = PaymentStatusSerializer
    
    def get(self, request, payment_id):
        try:
            payment = Payment.objects.get(id=payment_id)
            return Response({
                'payment': PaymentStatusSerializer(payment).data,
                'status': 'success',
                'message': 'Payment Retrieved Successfully',
            }, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({
                'message': 'Payment not found',
            }, status=status.HTTP_404_NOT_FOUND)