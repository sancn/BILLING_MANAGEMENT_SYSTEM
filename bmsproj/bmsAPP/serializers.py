from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class DefaulModelSerializer(serializers.ModelSerializer):
  @property
  def request(self):
      return self.context.get('request')

class ClientSerializer(DefaulModelSerializer):
    # count=serializers.SerializerMethodField()
    
    # def get_count(self,obj):
    #     return Client.objects.count()
    
    class Meta:
        model=Client
        fields='__all__'
        # fields = ['id', 'created_at', 'modified_at', 'name', 'email', 'contact', 'domain', 'expiry_date', 'organization_size', 'country', 'status', 'count']

        

class SubscriptionPlanSerializer(DefaulModelSerializer):
    class Meta:
        model=SubscriptionPlan
        fields='__all__'



class  SubscriptionSerializer(DefaulModelSerializer):
    class Meta:
        model=Subscription
        fields='__all__'
      
class MetricsSerializer(DefaulModelSerializer):
    class Meta:
        model=Metrics
        fields='__all__'

class HistorySerializer(DefaulModelSerializer):
    class Meta:
        model=History
        fields='__all__'