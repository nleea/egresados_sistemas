from celery import shared_task
from django.core.mail import send_mail
from configuration import settings
from django.template.loader import render_to_string
from qr_code.views import QRCodeOptions

@shared_task(bind=True, rate_limit='50/m', autoretry_for=(Exception,), retry_kwargs={'max_retries': 5})
def send_notification_mail(self, target_mail, message):
    try:

        context = dict(my_options=QRCodeOptions(
            size='t', border=6, error_correction='L'))

        msg_html = render_to_string(
            'templates/email.html', context=context)

        mail_subject = "Welcome on Board!"
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=target_mail,
            fail_silently=False,
            html_message=msg_html
        )
        return "Done"

    except Exception as e:
        raise e
