from django.conf import settings
from django.core.mail import send_mail
from Backend.utils.encryption import rndName
from django.core.cache import cache
def send(emails):
    code = rndName(6)
    send_mail(subject='验证码通知',
    message='【某网站】验证码: ' + code +'。验证码有效期为3分钟，请尽快验证。',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=emails)
    cache.set(emails[0],code,180)
