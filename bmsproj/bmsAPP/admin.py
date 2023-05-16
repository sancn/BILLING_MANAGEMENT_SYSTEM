from django.contrib import admin
from . import models

# Register your models here.
mymodels=[models.Client,models.SubscriptionPlan,models.Subscription,models.Metrics,models.History]
# mymodels=[Client,SubscriptionPlan,Subscription,Metrics]

admin.site.register(mymodels)