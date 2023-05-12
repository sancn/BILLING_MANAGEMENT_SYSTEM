############################
#############################

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from bmsAPP.models import Client

def send_expiry_reminder():
    today = date.today()
    expiry_date_threshold = today + relativedelta(days=5)
    
    # Find clients whose trail expires within 5 days
    clients = Client.objects.filter(expiry_date__lte=expiry_date_threshold)
    
    # Send emails to the clients
    for client in clients:
        subject = 'Trial Expiration Reminder'
        message = """
        Dear Sir/Madam,

        I hope this email finds you well. I wanted to reach out to inform you that your free trial with "DA Real Technology" is expiring on f"{expiry_date}". We hope you've had a positive experience thus far and that our [product/service] has met your expectations.

        As a valued user, we wanted to remind you that your free trial period will expire on 2023-5-30. This means that you will no longer have access to all the features and benefits our [product/service] offers unless you upgrade to a paid subscription.

        By subscribing to our premium plan, you'll unlock a host of additional features and enjoy uninterrupted access to our [product/service]. Our paid users also receive priority customer support and exclusive discounts on future upgrades.

        To continue using our [product/service] seamlessly, I encourage you to take advantage of our special offer.

        Should you have any questions or need assistance with the upgrade process, please don't hesitate to reach out to our dedicated support team. They are available from 9 AM to 6 PM and will be more than happy to assist you.

        Thank you for choosing "AAYULOGIC". We value your feedback and would love to hear about your experience with our [product/service]. Feel free to share any suggestions or insights you may have, as they help us enhance our offerings and provide the best possible solutions to our customers.

        We appreciate your consideration and look forward to continuing our partnership. Upgrade now and ensure uninterrupted access to all the benefits of our [product/service].

Best regards,
Realhrsoft
realhrsoft@gmail.com
"""
        from_email = 'realhrsoft.com.np'
        to_email = [client.email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)




##############################
################################

# from datetime import date
# from dateutil.relativedelta import relativedelta
# from django.core.mail import send_mass_mail
# from django_q.models import Schedule
# from bmsAPP.models import Client

# def email_task():
#     expiry_date = date.today() + relativedelta(days=5)
    
#     # Find clients whose trail expires in 5 days
#     clients = Client.objects.filter(expiry_date=expiry_date)
    
#     # Send emails to the clients
#     messages = []
#     for client in clients:
#         message = (
#             'Trail Expiration Reminder',
#             'Your trail will expire soon.',
#             'sender@example.com',
#             [client.email],
#         )
#         messages.append(message)

#     send_mass_mail(messages, fail_silently=False)
    
#     # Schedule the task to repeat every 5 days
#     Schedule.objects.create(
#         func='email_task.email_task',
#         schedule_type=Schedule.DAILY,
#         repeats=5,
#     )

###################################
####################################
###################################
# from datetime import date
# from dateutil.relativedelta import relativedelta
# from django_q.models import Schedule

# from django.core.mail import send_mass_mail
# from bmsAPP.models import Client
# from django.core.mail import EmailMessage

# def send_expiry_reminder():
#     expiry_date = date.today() + relativedelta(days=5)
    
#     # Find clients whose trail expires in 5 days
#     clients = Client.objects.filter(expiry_date=expiry_date)
    
#     # Send emails to the clients
#     for client in clients:
#         subject = 'Trail Expiration Reminder'
#         message = 'Your trail will expire soon.'
#         from_email = 'abc@example.com'
#         to_email = [client.email]
#         send_expiry_remindersilently=False

################ yo nagarda ni hunxa
#Schedule the task to repeat every 5 days
        # Schedule.objects.create(
        #     func='bmsAPP.tasks.email_task.send_expiry_reminder',
        #     schedule_type=Schedule.DAILY,
        #     repeats=5,
        # )
###########################
###############################
###################################

