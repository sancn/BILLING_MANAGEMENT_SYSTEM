from warnings import filters
from django.shortcuts import render
from .serializers import ClientSerializer,SubscriptionPlanSerializer,SubscriptionSerializer,MetricsSerializer,HistorySerializer
from  rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import status
from .models import *
from .models import History
# importing filters
from django_filters import rest_framework as filters
from .filters import ClientFilter,SubscriptionFilter
from rest_framework.decorators import action

# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    
    def list(self, request, *args, **kwargs):
       response = super().list(request, *args, **kwargs)
       count = self.queryset.count()
       small_count = self.queryset.filter(organization_size='s').count()
       medium_count = self.queryset.filter(organization_size='m').count()
       large_count = self.queryset.filter(organization_size='l').count()
       response_data = response.data
       response_data.extend([{"count": count, "small": small_count, "medium": medium_count, "large": large_count}])
       response.data = response_data
       return response

    #Deleting data from serializer
    def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      History.objects.get_or_create(remarks=instance.name)
      self.perform_destroy(instance)
      return Response({'msg':'Delete vayo gaich'},status=HTTP_204_NO_CONTENT)
    

    @action(detail=False, methods=['GET'],url_path='unverify')
    def unverified(self, request):
      unverified_client=self.queryset.filter(status='unveri')
      serializer = ClientSerializer(unverified_client, many=True)
      #  serializer=self.get_serializer(unverified_client,many=True)

      return Response(serializer.data)
   
    
class SubscriptionPlanViewset(viewsets.ModelViewSet):
  queryset=SubscriptionPlan.objects.all()
  serializer_class=SubscriptionPlanSerializer

class SubscriptionViewset(viewsets.ModelViewSet):
   queryset=Subscription.objects.all()
   serializer_class=SubscriptionSerializer

class MetricsViewset(viewsets.ModelViewSet):
   queryset=Metrics.objects.all()
   serializer_class=MetricsSerializer

class HistoryViewset(viewsets.ModelViewSet):
   queryset=History.objects.all()
   serializer_class=HistorySerializer

 

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