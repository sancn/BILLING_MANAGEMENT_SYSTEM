from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .models import *

from . import views
router = DefaultRouter()
router.register('Client', views.ClientViewset,basename='clint')
router.register('SubscriptionPlan', views.SubscriptionPlanViewset,basename='subplan')
router.register('Subscription', views.SubscriptionViewset,basename='sub')
router.register('Metrics',views.MetricsViewset,basename='metri')

urlpatterns = [
    path('', include(router.urls)),
]