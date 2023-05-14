from django.db import models

# Regex validators for phonr number
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.forms import ValidationError


# Create your models here.

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

"""This is a client detail model
    Which gives the client detail"""

## Domain name validation 
def validate_domain(value):
    if not value.endswith('.realhrsoft.com.np'):
        raise ValidationError("Domain name should end with 'realhrsoft.com.np'.")
class Client(BaseModel):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    # phone_regex = RegexValidator(regex=r'^\+?977?\d{10}$', 
                                #  message="Phone number must be entered in the format: '+9779999999999'. 10 digits allowed.")

    contact=models.PositiveIntegerField()

    domain=models.CharField(validators=[validate_domain],max_length=200)
    expiry_date = models.DateField()
    org_size_choices=(
        ('s','Small'),
        ('m','Medium'),
        ('l','Large'),


    )
    organization_size=models.CharField(choices=org_size_choices,max_length=50)
    country=models.CharField(max_length=50)
    verify_unverified_choices=(
        ('veri','Verified'),
        ('unveri','unverified'),
    )
    status=models.CharField(max_length=200,choices=verify_unverified_choices,default='unveri')

    # def __str__(self):
    #     return self.name
    
"""This is Subscription plan model.
  It gives the no.of user in the organizATION AND 
  organization have a choices to choose model and 
  price is based on pay per use model"""    
class SubscriptionPlan(BaseModel):
    no_of_user=models.PositiveIntegerField()
    modules_choices=(
        ('P','Payroll'),
        ('L','Leave'),
        ('A','Appraisal'),
        ('At','Attendance'),
    )
    module=models.CharField(choices=modules_choices,max_length=200)
    prices=models.DecimalField(max_digits=20,decimal_places=2)

    
"""SUbscription model inherits the client model
   it also gives subscription status and interval of subscription"""
class Subscription(BaseModel):
    client=models.OneToOneField(Client,on_delete=models.CASCADE)
    paid_due_choices=(
        ('pd','paid'),
        ('du','due'),

    )
    status=models.CharField(max_length=200,choices=paid_due_choices,default='du')
    model_interval_choices=(
        ('1','One Month'),
        ('3','Three Month'),
        ('6','Six Month'),
        ('12','One Year'),
    )
    model_interval=models.CharField(choices=model_interval_choices,default='1',max_length=200)
    subscription_plan=models.OneToOneField(SubscriptionPlan,on_delete=models.CASCADE)

"""This nodel calculate the Metrics of the pfrom django.core.validators import MinValueValidator
roject"""
class Metrics(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    ram_usage = models.FloatField(validators=[MinValueValidator(0)],max_length=200)
    hard_disk_usage = models.FloatField(validators=[MinValueValidator(0)],max_length=200)
    number_of_users = models.PositiveIntegerField()
    number_of_organizations = models.PositiveIntegerField()


