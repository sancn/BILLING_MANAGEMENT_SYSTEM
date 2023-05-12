from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .models import *

from . import views
router = DefaultRouter()
router.register('Client', views.ClientViewset.as_view,basename='clint')
router.register('SubscriptionPlan', views.SubscriptionPlanViewset.as_view,basename='subplan')
router.register('Subscription', views.SubscriptionViewset.as_view,basename='sub')
router.register('Metrics',views.MetricsViewset,basename='metri')

urlpatterns = [
    path('', include(router.urls)),
]