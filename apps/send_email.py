from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from configuration import settings
from django.template.loader import render_to_string
import qrcode
import qrcode.image.svg
from io import BytesIO
import base64

@shared_task(bind=True, rate_limit='50/m', autoretry_for=(Exception,), retry_kwargs={'max_retries': 5})
def send_notification_mail(self,target_mail, message):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = f"http://127.0.0.1:8000/inscripciones/?evento={1}/?user={1}" # La información que se desea codificar en el código QR
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        img.save(buffer)
        image_buffer = buffer.getvalue()
        image_base64 = base64.b64encode(image_buffer).decode('utf-8')

        plaintext = render_to_string(
            'email.txt', context={'image': image_base64})
        htmly = render_to_string('email.html', context={'image': image_base64})

        subject, from_email, to = 'hello', settings.EMAIL_HOST_USER, target_mail
        msg = EmailMultiAlternatives(subject, plaintext, from_email, to)
        msg.attach_alternative(htmly, "text/html")
        msg.send()
        return "Done"

    except Exception as e:
        raise e
