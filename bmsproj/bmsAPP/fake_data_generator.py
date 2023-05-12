from django.core.validators import RegexValidator
from django.forms import ValidationError
import random
from faker import Faker
from decimal import Decimal
from .models import SubscriptionPlan, Subscription, Metrics, Client

fake = Faker()

def generate_fake_data():
  # Generate fake data for the Client model
  for _ in range(30):
    name = fake.name()
    email = fake.email()
    contact = fake.phone_number()
    domain = name.lower().replace(" ", "") + ".realhrsof.com.np"
    expiry_date = fake.date_between(start_date="+1y", end_date="+2y")
    organization_size = fake.random_element(['s', 'm', 'l'])
    country = fake.country()
    status = fake.random_element(['veri', 'unveri'])

    Client.objects.create(
        name=name,
        email=email,
        contact=9851106875,
        domain=domain,
        expiry_date=expiry_date,
        organization_size=organization_size,
        country=country,
        status=status
    )

  # Generate fake data for the SubscriptionPlan model
  for _ in range(30):
    no_of_user = fake.random_int(min=1, max=100)
    module = fake.random_element(['P', 'L', 'A', 'At'])
    prices = Decimal(random.randint(150000, 300000) / 100)

    SubscriptionPlan.objects.create(
        no_of_user=no_of_user,
        module=module,
        prices=prices
    )

  # Generate fake data for the Subscription model
  clients = Client.objects.all()
  subscription_plans = SubscriptionPlan.objects.all()
  for i in range(30):
    client = clients[i]
    subscription_plan = subscription_plans[i]
    status = fake.random_element(['pd', 'du'])
    model_interval = fake.random_element(['1', '3', '6', '12'])

    Subscription.objects.create(
        client=client,
        status=status,
        model_interval=model_interval,
        subscription_plan=subscription_plan
    )

  # Generate fake data for the Metrics model
  clients = Client.objects.all()
  for client in clients:
    ram_usage = fake.pyfloat(min_value=0, max_value=1000)
    hard_disk_usage = fake.pyfloat(min_value=0, max_value=1000)
    number_of_users = fake.random_int(min=1, max=100)
    number_of_organizations = fake.random_int(min=1, max=100)

    Metrics.objects.create(
        client=client,
        ram_usage=ram_usage,
        hard_disk_usage=hard_disk_usage,
        number_of_users=number_of_users,
        number_of_organizations=number_of_organizations
    )


