from django_filters import rest_framework as filters
from .models import Client,Subscription
class ClientFilter(filters.FilterSet):
    class Meta:
        model=Client
        fields={
            'expiry_date':['exact','lte','gte'],
            'subscription__status':['exact'],
        }

class SubscriptionFilter(filters.FilterSet):
    class Meta:
        model=Subscription
        fields={
            'status':['exact'],

        }