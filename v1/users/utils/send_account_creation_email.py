from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_account_verification_email(request, user, token, uid):
    mail_subject = 'Complete your account setup'
    message = render_to_string(f'{settings.BASE_DIR}/v1/users/templates/account_creation_mail.html', {
        'user': user,
        'domain': request.META.get('HTTP_ORIGIN'),
        'uid': uid,
        'token': token
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
