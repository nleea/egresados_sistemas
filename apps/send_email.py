import tempfile
from celery import shared_task
from django.core.mail import send_mail,EmailMultiAlternatives
from configuration import settings
from django.template.loader import render_to_string
import qrcode
import qrcode.image.svg
from io import BytesIO
import base64
from django.utils.html import strip_tags

@shared_task(bind=True, rate_limit='50/m', autoretry_for=(Exception,), retry_kwargs={'max_retries': 5})
def send_notification_mail(self,target_mail, message):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = f"http://127.0.0.1:8000/inscripciones/?evento={1}/?user={1}" # La información que se desea codificar en el código QR
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as img_file:
            img.save(img_file)
            img_file.seek(0)
            image_data = img_file.read()
            
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        plaintext = render_to_string(
            'email.txt', context={'image': image_base64})
        htmly = render_to_string('email.html', context={'image': image_base64})
        text_content = strip_tags(htmly)

        data = 'https://www.example.com'

        subject = 'Correo electrónico con código QR'
        message = 'Este correo electrónico contiene un código QR'
        from_email = 'sender@example.com'
        recipient_list = ['recipient@example.com']
        
        # Adjuntar la imagen del código QR al correo electrónico
        image_filename = 'qr_code.png'
        image_content_type = 'image/png'
        image_content_id = 'qr_code'
        attachments = [(image_filename, image_base64, image_content_type, {'Content-ID': image_content_id})]

        # Enviar el correo electrónico
        msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        msg.attach(filename=image_filename, content=image_data, mimetype=image_content_type)
        msg.attach_alternative(htmly, "text/html")
        msg.send()
        return "Done"

    except Exception as e:
        raise e
