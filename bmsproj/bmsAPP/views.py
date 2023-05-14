from warnings import filters
from django.shortcuts import render
from .serializers import ClientSerializer,SubscriptionPlanSerializer,SubscriptionSerializer,MetricsSerializer
from  rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import *

# importing filters
from django_filters import rest_framework as filters
from .filters import ClientFilter,SubscriptionFilter

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


#filter the result
class  ClientFilterViewset(viewsets.ModelViewSet):
   queryset=Client.objects.all()
   serializer_class=ClientSerializer
   filter_backends = [filters.DjangoFilterBackend] 
   ordering_fields=['created_at','modified_at']
   filterset_class=ClientFilter


class SubscriptionFilterViewset(viewsets.ModelViewSet):
   queryset = Subscription.objects.all()
   serializer_class = SubscriptionSerializer
   filter_backends = [filters.DjangoFilterBackend] 
   ordering_fields = ['created_at', 'modified_at']
   filterset_class = SubscriptionFilter