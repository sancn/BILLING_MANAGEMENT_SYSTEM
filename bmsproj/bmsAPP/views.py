from django.shortcuts import render
from .serializers import ClientSerializer,SubscriptionPlanSerializer,SubscriptionSerializer,MetricsSerializer
from  rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import *

# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

class SubscriptionPlanViewset(viewsets.ModelViewSet):
  queryset=SubscriptionPlan.objects.all()
  serializer_class=SubscriptionPlanSerializer

class SubscriptionViewset(viewsets.ModelViewSet):
   queryset=Subscription.objects.all()
   serializer_class=SubscriptionSerializer

class MetricsViewset(viewsets.ModelViewSet):
   queryset=Metrics.objects.all()
   serializer_class=MetricsSerializer