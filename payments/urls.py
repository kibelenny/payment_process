from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.InitializePayment.as_view(), name='process_payment'),
    path('payments/<uuid:payment_id>/', views.PaymentStatus.as_view(), name='payment_status')
]