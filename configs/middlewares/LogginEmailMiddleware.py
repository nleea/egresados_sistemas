from django.utils.log import AdminEmailHandler

from celery import shared_task
from django.core.mail import EmailMessage
import logging

logger = logging.Logger(__name__)

ADMINS = [
    ("Nelson", "egresados398@gmail.com"),
    # ("Oscar", "oiarregoces@uniguajira.edu.co"),
]


@shared_task(
    bind=True,
    rate_limit="50/m",
    autoretry_for=(Exception,),
)
def email_deliveri(self, subject, message):
    mailer = EmailMessage(
        subject, message, "egresados398@gmail.com", [x[1] for x in ADMINS]
    )
    try:
        mailer.send()
    except Exception as e:
        print(e)


class CustomEmailHandler(AdminEmailHandler):
    def send_mail(self, subject, message, *args, **kwargs):
        email_deliveri.delay(subject, message)  # type:ignore


