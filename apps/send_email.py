import tempfile
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from configuration import settings
from django.template.loader import render_to_string
import qrcode
import qrcode.image.svg
import base64
from django.utils.html import strip_tags


@shared_task(
    bind=True,
    rate_limit="50/m",
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 5},
)
def send_notification_mail(self, target_mail, id, evento):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)  # type:ignore
        # La información que se desea codificar en el código QR
        data = f"http://44.203.185.252/eventos/inscripciones/asistencia/?evento={evento}&user={id}"
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as img_file:
            img.save(img_file)
            img_file.seek(0)
            image_data = img_file.read()

        image_base64 = base64.b64encode(image_data).decode("utf-8")

        htmly = render_to_string("email.html", context={"image": image_base64})
        text_content = strip_tags(htmly)

        # Datos para el correo
        subject = "Correo electrónico con código QR"
        from_email = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives(subject, text_content, from_email, target_mail)

        # Adjuntar la imagen del código QR al correo electrónico
        image_filename = "qr_code.png"
        image_content_type = "image/png"
        msg.attach(
            filename=image_filename, content=image_data, mimetype=image_content_type
        )
        msg.attach_alternative(htmly, "text/html")

        # Enviar el correo electrónico
        msg.send()
        return "Done"

    except Exception as e:
        raise e


@shared_task(
    bind=True,
    rate_limit="50/m",
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 5},
)
def send_confirm_mail(self, target_mail, evento):
    print(target_mail, evento, "entro")
    try:
        subject = "Correo electrónico con código QR"
        from_email = settings.EMAIL_HOST_USER
        url = f"http://44.203.185.252/eventos/inscripciones/confirmar/asistencia/?evento={evento}"
        htmly = render_to_string("confirm_mensaje.html", context={"url": url})
        text_content = strip_tags(htmly)
        msg = EmailMultiAlternatives(subject, text_content, from_email, target_mail)
        msg.attach_alternative(htmly, "text/html")
        msg.send()
        return "Done"

    except Exception as e:
        raise e


def send_email_list(userList, evento, custom_email):
    for _, x in enumerate(userList):
        send_confirm_mail.delay(target_mail=[x.email], evento=evento)  # type: ignore
    for x in custom_email:
        send_confirm_mail.delay(target_mail=[x], evento=evento)  # type:ignore
