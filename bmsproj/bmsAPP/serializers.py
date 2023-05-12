from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *

class DefaulModelSerializer(serializers.ModelSerializer):
  @property
  def request(self):
      return self.context.get('request')
  
  # def validate(self, attrs):
  #   #  user = self.context.user
  #   user = self.request.user

  #   return super().validate(attrs)
  
# ser = DefaulModelSerializer({'a':2,'b':5}, context={'request': self.request})
# ser.is_valid()
# ser.save()

class ClientSerializer(DefaulModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

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