# BILLING MANAGEMENT SYSTEM
##### The Billing Management System is a Django-based project designed to handle client details, subscription plans, and metrics for a billing management application. 

## Features
The Billing Management System offers the following features:

1. **Client Management:** Easily manage client details, including their name, email, contact information, domain, expiry date, organization size, country, and verification status.

2. **Subscription Plans:** Define various subscription plans with different numbers of users, module choices (such as Payroll, Leave, Appraisal, and Attendance), and pricing based on a pay-per-use model.

3. **Subscription Management:** Track and manage client subscriptions, including their status (paid or due), interval (monthly, quarterly, semi-annually, or annually), and associated client and subscription plan.

4. **Metrics Calculation:** Calculate and store metrics related to the project, such as RAM usage, hard disk usage, number of users, and number of organizations.

5. **Email Notifications:** The system automatically sends email notifications to clients whose free trial period is ending within the next five days, reminding them to subscribe to a suitable plan.

## Table of Contents
- Installation
- Usage
- Models
- Serializers
- URLs
- Filters
## Installation
1. Clone the repository to your local machine or server:
   [BILLING_MANAGEMENT_SYSTEM ](https://github.com/sancn/BILLING_MANAGEMENT_SYSTEM)
 
2. Navigate to the project directory:
   <prep>
   $ cd billing_management_system
   </prep>
3. Install the required dependencies. It is recommended to use a virtual environment:
   <pre>
   $ sudo apt-get install virtualenv
   $ virtualenv env (where, env---> name of the virtual enviroment)
   $ source env/bin/activate
   $ pip install -r requirements.txt
   </pre>
   
 4. Set up the database by running migrations:
    <pre>
      $ python manage.py migrate
   </pre>
   
## Usage

To start the Django development server, use the following command:
<pre>
   $ python manage.py runserver
 </pre>
 You can access the Billing Management System application by visiting <pre> http://localhost:8000/bms/</pre> in your web browser.

## Models
The Billing Management System consists of the following models:
- **Client:** Represents client details such as name, email, contact, domain, expiry date, organization size, country, and status.
- **SubscriptionPlan:** Defines subscription plan details including the number of users, module choices, and prices.
- **Subscription:** Represents a client's subscription status and interval, along with the associated client and subscription plan.
- **Metrics:** Stores metrics data for the project, including RAM usage, hard disk usage, number of users, and number of organizations.

## Serializers

The project includes serializers to convert model instances to JSON representations and vice versa. The serializers provided are:

- **ClientSerializer:** Serializes and deserializes Client model instances.
- **SubscriptionPlanSerializer:** Serializes and deserializes SubscriptionPlan model instances.
- **SubscriptionSerializer:** Serializes and deserializes Subscription model instances.
- **MetricsSerializer:** Serializes and deserializes Metrics model instances.

## URLs

The project defines the following URLs:

- */bms/:* Base URL for the Billing Management System application.
- */bms/Client/:* URL for managing client details.
- */bms/SubscriptionPlan/:* URL for managing subscription plans.
- */bms/Subscription/:* URL for managing subscriptions.
- */bms/Metrics/:* URL for managing metrics.

## Filters
The project includes filters to allow easy querying of the models. The available filters are:

- **ClientFilter:** Allows filtering client details based on expiry date and subscription status.
- **SubscriptionFilter:** Allows filtering subscriptions based on status.
You can use these filters by appending query parameters to the respective API endpoints.



